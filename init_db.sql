DROP TABLE if EXISTS gaming;
CREATE TABLE gaming (
    exe_name text,
    session_start real,
    session_end real,
    time_played real,
    PRIMARY KEY (exe_name, session_start) );

INSERT into gaming values ('MK11.exe', 2459072.54339, NULL, NULL);
INSERT into gaming values ('NBA2K19.exe', 2459070.34927, 2459070.47427, .125);
INSERT into gaming values ('MK11.exe', 2459070.14094, 2459070.1826, 0.04166);
INSERT into gaming values ('NSF14.exe', 2459069.4326, 2459069.51594, 0.08334);
INSERT into gaming values ('FarCry5.exe', 2459069.3076, 2459069.37566, 0.06806);
INSERT into gaming values ('mgsvtpp.exe', 2459067.21594, 2459067.34094, 0.125);


