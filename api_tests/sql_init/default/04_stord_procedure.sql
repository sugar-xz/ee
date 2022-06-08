\c apiserver;

BEGIN;
    DO
    $body$
    DECLARE
    
        _fk_logic_rule text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_rule' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_snap text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_snap' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_event text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_event' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_eventbackup text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_eventbackup' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_cameravideo text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_cameravideo' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_camerasavedvideo text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_camerasavedvideo' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_cameralocation text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_cameralocation' AND column_name = 'camera_id' AND constraint_name like '%fk%'
        );

        _fk_logic_medium text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_medium' AND column_name = 'event_id' AND constraint_name like '%fk%'
        );

        _fk_guard_case text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'guard_case' AND column_name = 'event_id' AND constraint_name like '%fk%'
        );

        _fk_logic_mediumbackup text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'logic_mediumbackup' AND column_name = 'event_id' AND constraint_name like '%fk%'
        );

        _fk_guard_note text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'guard_note' AND column_name = 'case_id' AND constraint_name like '%fk%'
        );

        _fk_guard_casemedium text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'guard_casemedium' AND column_name = 'case_id' AND constraint_name like '%fk%'
        );

        _fk_guard_casehistory text := (
            SELECT constraint_name
            FROM information_schema.key_column_usage
            WHERE table_name = 'guard_casehistory' AND column_name = 'case_id' AND constraint_name like '%fk%'
        );

    BEGIN
    
        EXECUTE 'ALTER TABLE logic_rule DROP CONSTRAINT ' || _fk_logic_rule ;
        EXECUTE 'ALTER TABLE logic_rule ADD CONSTRAINT ' || _fk_logic_rule ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_snap DROP CONSTRAINT ' || _fk_logic_snap ;
        EXECUTE 'ALTER TABLE logic_snap ADD CONSTRAINT ' || _fk_logic_snap ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_event DROP CONSTRAINT ' || _fk_logic_event ;
        EXECUTE 'ALTER TABLE logic_event ADD CONSTRAINT ' || _fk_logic_event ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_eventbackup DROP CONSTRAINT ' || _fk_logic_eventbackup ;
        EXECUTE 'ALTER TABLE logic_eventbackup ADD CONSTRAINT ' || _fk_logic_eventbackup ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_cameravideo DROP CONSTRAINT ' || _fk_logic_cameravideo ;
        EXECUTE 'ALTER TABLE logic_cameravideo ADD CONSTRAINT ' || _fk_logic_cameravideo ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_camerasavedvideo DROP CONSTRAINT ' || _fk_logic_camerasavedvideo ;
        EXECUTE 'ALTER TABLE logic_camerasavedvideo ADD CONSTRAINT ' || _fk_logic_camerasavedvideo ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_cameralocation DROP CONSTRAINT ' || _fk_logic_cameralocation ;
        EXECUTE 'ALTER TABLE logic_cameralocation ADD CONSTRAINT ' || _fk_logic_cameralocation ||
        ' FOREIGN KEY (camera_id) REFERENCES logic_camera(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_medium DROP CONSTRAINT ' || _fk_logic_medium ;
        EXECUTE 'ALTER TABLE logic_medium ADD CONSTRAINT ' || _fk_logic_medium ||
        ' FOREIGN KEY (event_id) REFERENCES logic_event(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE guard_case DROP CONSTRAINT ' || _fk_guard_case ;
        EXECUTE 'ALTER TABLE guard_case ADD CONSTRAINT ' || _fk_guard_case ||
        ' FOREIGN KEY (event_id) REFERENCES logic_event(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE logic_mediumbackup DROP CONSTRAINT ' || _fk_logic_mediumbackup ;
        EXECUTE 'ALTER TABLE logic_mediumbackup ADD CONSTRAINT ' || _fk_logic_mediumbackup ||
        ' FOREIGN KEY (event_id) REFERENCES logic_eventbackup(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE guard_note DROP CONSTRAINT ' || _fk_guard_note ;
        EXECUTE 'ALTER TABLE guard_note ADD CONSTRAINT ' || _fk_guard_note ||
        ' FOREIGN KEY (case_id) REFERENCES guard_case(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE guard_casemedium DROP CONSTRAINT ' || _fk_guard_casemedium ;
        EXECUTE 'ALTER TABLE guard_casemedium ADD CONSTRAINT ' || _fk_guard_casemedium ||
        ' FOREIGN KEY (case_id) REFERENCES guard_case(id) ON DELETE CASCADE';

        EXECUTE 'ALTER TABLE guard_casehistory DROP CONSTRAINT ' || _fk_guard_casehistory ;
        EXECUTE 'ALTER TABLE guard_casehistory ADD CONSTRAINT ' || _fk_guard_casehistory ||
        ' FOREIGN KEY (case_id) REFERENCES guard_case(id) ON DELETE CASCADE';

    END
    $body$;
COMMIT;
