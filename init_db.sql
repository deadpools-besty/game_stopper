CREATE TABLE gaming (
    exe_name text,
    session_start real,
    session_end real,
    time_played real,
    PRIMARY KEY (exe_name, session_start) );