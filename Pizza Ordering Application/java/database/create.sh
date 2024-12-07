#!/bin/bash
export PGPASSWORD='postgres1'
BASEDIR=$(dirname $0)
DATABASE=final_capstone
psql -U postgres -f "$BASEDIR/sql/dropdb.sql" &&
createdb -U postgres $DATABASE &&
psql -U postgres -d $DATABASE -f "$BASEDIR/sql/schema.sql" &&
psql -U postgres -d $DATABASE -f "$BASEDIR/sql/data.sql" &&
psql -U postgres -d $DATABASE -f "$BASEDIR/sql/user.sql"