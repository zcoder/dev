#!/usr/bin/env bash

if [[ $1 != "" ]]; then
sqlite3 -csv $1 'CREATE TRIGGER if not exists Messages_update_hook AFTER UPDATE OF body_xml    ON Messages begin update Messages set body_xml = case when new.body_xml <> "" then new.body_xml else old.body_xml end where id=new.id; end;'
fi;
