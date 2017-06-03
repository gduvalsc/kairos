Within this directory, a lot of scripts to collect data on production systems. The result is a zip or a tar.gz file to be uploaded into Kairos

## Data collection for Oracle

Starting from Oracle version 10 and upper, there are AWR and ASH availables but they must be used only if the the pack "Oracle diagnostic pack" has been bought by the customer.

So KAIROS can collect data above AWR and ASH if the customer has the right to use them, but KAIROS can collect data above STATSPACK and another Free Software (B-ASH, see https://marcusmonnig.wordpress.com/bash/) if the customer doesn't have the right to use "Oracle diagnostic pack".

The script "kairosora.ksh" is available to collect data both  AWR or STATSPACK and B-ASH.

###### Oracle Data Collection for Kairos

The script must be transfered to a system where the Oracle Database resides. Some Oracle installations don't use the "oraenv" mechanism to switch between Oracle contexts.

If "oraenv" is used, it's better tu use the collect script with the flag "-oraenv".

If "oraenv" isn't used or doesn't work for any reason, the Oracle data collection script for KAIROS must be used when the Oracle context has been setup manually.

Oracle data Collection when AWR is allowed

The general form of the command to be run to capture a day of activity is:

```
ksh /TOOLDIR/kairosora.ksh -sid:MYINSTANCE -day:YYYY-MM-DD -awr -lvl:3 -zip -grp:GGGG -dir:DDDD
```

where

TOOLDIR is the directory in which the data collection script has been put

MYINSTANCE is the name of the Oracle instance

YYYY-MM-DD is the day to be extracted (ex : 2016-08-20 for August 2016, 20)

GGGG (not mandatory, default value UNKNOWN is a symbol identifying the company)

DDDD is the directory in which the result (tar file or zip file) will be written.


If the -day parameter is not specified, data is extracted from the day before. This is especially useful when the command is triggered through a scheduler like "cron". In this case, the same command executed every day will produce a different result each day. This is a way to automate the data collection.

Oracle data Collection when AWR is NOT allowed

In this case, the general form of the command is:

```
ksh /TOOLDIR/kairosora.ksh -sid:MYINSTANCE -day:YYYY-MM-DD -pwd:PPPP -bash -zip -grp:GGGG -dir:DDDD
```

The difference with the invocation in the AWR context is:

-awr and -lvl have been removed (meaning STATSPACK is required)

-bash is a flag to indicate that collection over B-ASH is required

PPPP is the PERFSTAT password is the case of STATSPACK. The default value is PERFSTAT.

If the PERSTAT password is not PERFSTAT and if the customer don't want to pass the password as an argument of the command, the default password must be changed in the provided KAIROS script.

###### STATSPACK installation

STASTSPACK is always available in Oracle 10, 11, 12, even if all STATSPACK functionalities have been replaced by AWR.

The documentation to install and configure Statspack is available at this address: https://docs.oracle.com/cd/B10501_01/server.920/a96533/statspac.htm

For example, on UNIX:

```
SQL>  CONNECT / AS SYSDBA
SQL>  define default_tablespace='TOOLS'
SQL>  define temporary_tablespace='TEMP'
SQL>  define perfstat_password='my_perfstat_password'
SQL>  @?/rdbms/admin/spcreate
```

We suggest to use SYSAUX as the default tablespace.

To automate the production of snapshots, the SPAUTO script must be used. The default value of one hour between each snapshot is enough if B-ASH is used in addition.

```
SQL>  CONNECT perfstat/my_perfstat_password
SQL>  @?/rdbms/admin/spauto
````

###### B-ASH installation

The package to install and configure B-ASH is provided in attachment.

Within the zip archive, there is a bashcreate_V8.sql to be run to activate B-ASH. In the header of the script there are comments to use the script.

We suggest to use SYSAUX as the default tablespace and start the B-ASH data collector immediately.

Once bashcreate_v8.sql has been completed, open a sql*plus session under bash/password_of_bash and issue the following request:

```
grant select on bash$hist_active_sess_history to perfstat;
```

B-ASH installation must be done after STATSPACK installation

## Data collection for PostgreSQL

In the PostgreSQL universe, data collection is done by adding an extension to a PostgreSQL database.

The software is delivered as  a "tar" archive. The name is "pgkairos.tar". This tar file must be copied on a system where PostgreSQL is running for exemple in the "/tmp" directory. From there, the administrator has to identify the directory where extensions are stored.

To identify the directory where the extension must be installed, run the following command:

```
$ psql -c "create extension very_improbable_name"
ERROR:  could not open extension control file "/usr/share/postgresql/9.5/extension/very_improbable_name.control": No such file or directory
```

The error message indicates the directory where the tar file must be extracted. In this example: "/usr/share/postgresql/9.5/extension"

So to install properly this PostgreSQL extension you have to:

```
$ cd /usr/share/postgresql/9.5/extension
$ tar xvf /tmp/pgkairos.tar
```

After that step, the extension is available. You can check the availability by running:

```
$ psql -c "select * from pg_available_extensions" | grep kairos
```

This extension must be then created in a new PostgreSQL database named "kairos"

```
$ psql -c "create database kairos"
$ psql -d kairos -c "create extension kairos"
$ psql -d kairos -c "\dp"
```

The last command lists all tables created through the extension. An exmaple of the list is:

```
                                      Access privileges
 Schema |          Name           | Type  | Access privileges | Column privileges | Policies 
--------+-------------------------+-------+-------------------+-------------------+----------
 public | config                  | table |                   |                   | 
 public | kairos_pg_stat_activity | table |                   |                   | 
 public | kairos_sql_text         | table |                   |                   | 
(3 rows)

```

From there, the extension is operational. A lot of functions are available to collect, purge or export data.

The "config" table keeps in mind the global parameters to control this process:

```
$ psql -d kairos -c "select * from config"
   param   | value 
-----------+-------
 enable    | true
 retention | 15.0
 directory | /tmp
(3 rows)
```

The kairos extension collects statistics if the "enable" poarameter is set to "true". Controlling the "enable" parameter allows to enable or disable the collect of statistics

The "retention" parameter specifies the number of days statistics are retained in the kairos database. When the purge is activated, it removes data older than "retention" days.

The "directory" parameter specifies the directory in which "exports" are generated.

All parameters of the config table can be read using the "get_param" function.
