-- 2015-11-22 18:25
-- anxolerd <anxolerd@outlook.com>
-- create initial tables

CREATE TABLE forms (
  id          SERIAL   NOT NULL,
  type        SMALLINT NOT NULL,
  description INTEGER,
  fields      JSONB    NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users (
  id                SERIAL NOT NULL,
  email             TEXT   NOT NULL,
  login_options     SMALLINT [],
  digest            VARCHAR(64),
  salt              VARCHAR(64),
  first_name        TEXT   NOT NULL,
  last_name         TEXT,
  age               INTEGER,
  gender            SMALLINT,
  permissions       SMALLINT [],
  facebook_token    TEXT,
  unique_identifier TEXT,
  PRIMARY KEY (id),
  UNIQUE (email),
  UNIQUE (unique_identifier)
);

CREATE TABLE images (
  id        SERIAL      NOT NULL,
  filename  UUID,
  extension VARCHAR(10) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (filename)
);

CREATE TABLE events (
  id                   SERIAL   NOT NULL,
  title                TEXT     NOT NULL,
  description          TEXT,
  organizer_id         INTEGER  NOT NULL,
  location             JSONB,
  datetime             TIMESTAMP WITH TIME ZONE,
  status               SMALLINT NOT NULL,
  max_registrations    INTEGER,
  registration_form_id INTEGER,
  feedback_form_id     INTEGER,
  logo_id              INTEGER,
  PRIMARY KEY (id),
  FOREIGN KEY (organizer_id) REFERENCES users (id),
  FOREIGN KEY (registration_form_id) REFERENCES forms (id),
  FOREIGN KEY (feedback_form_id) REFERENCES forms (id),
  FOREIGN KEY (logo_id) REFERENCES images (id)
);

CREATE TABLE registrations (
  id              SERIAL                   NOT NULL,
  user_id         INTEGER                  NOT NULL,
  event_id        INTEGER                  NOT NULL,
  status          SMALLINT                 NOT NULL,
  timestamp       TIMESTAMP WITH TIME ZONE NOT NULL,
  additional_info JSONB,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (event_id) REFERENCES events (id)
);
