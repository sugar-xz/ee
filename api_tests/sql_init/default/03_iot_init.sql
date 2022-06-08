--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

\c iot;

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Credential; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Credential" (
    id integer NOT NULL,
    service character varying(20) NOT NULL,
    credential_id character varying(50) NOT NULL,
    filename character varying(50) NOT NULL,
    signature character varying(100) NOT NULL,
    private_key text NOT NULL,
    public_key text,
    pending boolean DEFAULT false NOT NULL,
    loaded_at timestamp(6) with time zone,
    extra json DEFAULT '"[]"'::json NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    device character varying(80),
    assigned uuid
);


ALTER TABLE public."Credential" OWNER TO postgres;

--
-- Name: Credential_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Credential_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."Credential_id_seq" OWNER TO postgres;

--
-- Name: Credential_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Credential_id_seq" OWNED BY public."Credential".id;


--
-- Name: Device; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Device" (
    id character varying(80) NOT NULL,
    alias character varying(80) DEFAULT NULL::character varying,
    state character varying(15) DEFAULT 'offline'::character varying NOT NULL,
    "publicKey" character varying(1023) NOT NULL,
    fingerprint character varying(63),
    "localAddress" character varying(63) DEFAULT ''::character varying NOT NULL,
    "remoteAddress" character varying(63) DEFAULT ''::character varying NOT NULL,
    "defaultUsername" character varying(255) DEFAULT 'default'::character varying NOT NULL,
    install_uuid character varying(255),
    system character varying(20),
    platform character varying(20),
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    "userId" integer
);


ALTER TABLE public."Device" OWNER TO postgres;

--
-- Name: DeviceUpdate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."DeviceUpdate" (
    id integer NOT NULL,
    "deviceId" character varying(100) NOT NULL,
    service character varying(20) NOT NULL,
    "updateConfig" json NOT NULL,
    result json NOT NULL,
    "updateId" character varying(100) NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL
);


ALTER TABLE public."DeviceUpdate" OWNER TO postgres;

--
-- Name: DeviceUpdate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."DeviceUpdate_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."DeviceUpdate_id_seq" OWNER TO postgres;

--
-- Name: DeviceUpdate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."DeviceUpdate_id_seq" OWNED BY public."DeviceUpdate".id;


--
-- Name: Dist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Dist" (
    id integer NOT NULL,
    service character varying(20) NOT NULL,
    _system character varying(20),
    system character varying(20) NOT NULL,
    platform character varying(20) NOT NULL,
    version character varying(30) NOT NULL,
    level integer DEFAULT 0 NOT NULL,
    s3_bucket character varying(200) NOT NULL,
    s3_key character varying(200) NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL
);


ALTER TABLE public."Dist" OWNER TO postgres;

--
-- Name: Dist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Dist_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."Dist_id_seq" OWNER TO postgres;

--
-- Name: Dist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Dist_id_seq" OWNED BY public."Dist".id;


--
-- Name: Installation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Installation" (
    uuid character varying(255) NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    oem_uuid uuid
);


ALTER TABLE public."Installation" OWNER TO postgres;

--
-- Name: LevelRequirement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."LevelRequirement" (
    id integer NOT NULL,
    _system character varying(50),
    service character varying(20) NOT NULL,
    tag character varying(100) NOT NULL,
    system character varying(50) NOT NULL,
    platform character varying(20) NOT NULL,
    level integer DEFAULT 0 NOT NULL,
    version character varying(50) NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL
);


ALTER TABLE public."LevelRequirement" OWNER TO postgres;

--
-- Name: LevelRequirement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."LevelRequirement_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."LevelRequirement_id_seq" OWNER TO postgres;

--
-- Name: LevelRequirement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."LevelRequirement_id_seq" OWNED BY public."LevelRequirement".id;


--
-- Name: OEM; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."OEM" (
    uuid uuid NOT NULL,
    name character varying(100) NOT NULL,
    details json NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public."OEM" OWNER TO postgres;

--
-- Name: Resource; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Resource" (
    id integer NOT NULL,
    rtype character varying(15) NOT NULL,
    value character varying(15) NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    "deviceId" character varying(80),
    "userId" integer
);


ALTER TABLE public."Resource" OWNER TO postgres;

--
-- Name: Resource_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Resource_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."Resource_id_seq" OWNER TO postgres;

--
-- Name: Resource_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Resource_id_seq" OWNED BY public."Resource".id;


--
-- Name: SystemID; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SystemID" (
    "deviceId" character varying(100) NOT NULL,
    "systemId" character varying(100) NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL
);


ALTER TABLE public."SystemID" OWNER TO postgres;

--
-- Name: UpdateStatus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."UpdateStatus" (
    "deviceId" character varying(100) NOT NULL,
    "updateId" character varying(100) NOT NULL,
    "systemId" character varying(100) NOT NULL,
    data json NOT NULL,
    status character varying(30) NOT NULL,
    meta json,
    notified boolean DEFAULT false NOT NULL,
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL
);


ALTER TABLE public."UpdateStatus" OWNER TO postgres;

--
-- Name: User; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."User" (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    salt character varying(255) NOT NULL,
    iterations bigint NOT NULL,
    pass_hash character varying(685) NOT NULL,
    admin integer DEFAULT 0 NOT NULL,
    "resourceLimit" integer DEFAULT 10 NOT NULL,
    "resourceCount" integer DEFAULT 0 NOT NULL,
    "verificationHash" character varying(400),
    "createdAt" timestamp(6) with time zone NOT NULL,
    "updatedAt" timestamp(6) with time zone NOT NULL,
    "deletedAt" timestamp(6) with time zone,
    "pUserId" integer,
    permissions json
);


ALTER TABLE public."User" OWNER TO postgres;

--
-- Name: User_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."User_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public."User_id_seq" OWNER TO postgres;

--
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."User_id_seq" OWNED BY public."User".id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp(6) with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: Credential id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Credential" ALTER COLUMN id SET DEFAULT nextval('public."Credential_id_seq"'::regclass);


--
-- Name: DeviceUpdate id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DeviceUpdate" ALTER COLUMN id SET DEFAULT nextval('public."DeviceUpdate_id_seq"'::regclass);


--
-- Name: Dist id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Dist" ALTER COLUMN id SET DEFAULT nextval('public."Dist_id_seq"'::regclass);


--
-- Name: LevelRequirement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."LevelRequirement" ALTER COLUMN id SET DEFAULT nextval('public."LevelRequirement_id_seq"'::regclass);


--
-- Name: Resource id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Resource" ALTER COLUMN id SET DEFAULT nextval('public."Resource_id_seq"'::regclass);


--
-- Name: User id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."User" ALTER COLUMN id SET DEFAULT nextval('public."User_id_seq"'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: Credential; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Credential" (id, service, credential_id, filename, signature, private_key, public_key, pending, loaded_at, extra, "createdAt", "updatedAt", device, assigned) VALUES (1, 'robox', 'robot_dog_sr_20001', 'box.json', 'n/3ZVWYQ009bWcq3g1s0LyEiX2OqJY5g+KNBTz4+gAo=', '-----BEGIN PRIVATE KEY-----
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
Ohyp43XDDoFF5fFz9jG3NSMiN4er6zU=
-----END PRIVATE KEY-----
', NULL, false, NULL, '{}', '2019-05-30 02:28:43.196+08', '2019-05-30 02:28:43.196+08', NULL, NULL);
INSERT INTO public."Credential" (id, service, credential_id, filename, signature, private_key, public_key, pending, loaded_at, extra, "createdAt", "updatedAt", device, assigned) VALUES (5, 'robox', 'robot_dog_sr_20002', 'box.json', 'o4w0GJuvCu/Q++xLn+A49wa2HSOP+Ri33RLYx8SVUws=', '-----BEGIN PRIVATE KEY-----
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
g738XPx0YLbEsLZIt1WbpzcQbQ11uA==
-----END PRIVATE KEY-----
', NULL, false, NULL, '{}', '2019-05-30 02:28:43.198+08', '2019-05-30 02:28:43.198+08', '5df673f2-166a-4600-a5fe-d9d5d82b7790', NULL);
INSERT INTO public."Credential" (id, service, credential_id, filename, signature, private_key, public_key, pending, loaded_at, extra, "createdAt", "updatedAt", device, assigned) VALUES (2, 'robox', 'robot_dog_sr_20003', 'box.json', 'qa4Lwz9KW5MJrLqvM7Z3135rfQmu84xb1uuzeV+f/cg=', '-----BEGIN PRIVATE KEY-----
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
8T61l4j+z0YMp8EmitdxD6n4QDba3Zjv
-----END PRIVATE KEY-----
', NULL, false, '2019-05-30 03:11:50.645+08', '{}', '2019-05-30 02:28:43.199+08', '2019-05-30 03:11:50.645+08', 'bf3c4914-8529-4427-8e90-6cb2aa5d4d3d', NULL);
INSERT INTO public."Credential" (id, service, credential_id, filename, signature, private_key, public_key, pending, loaded_at, extra, "createdAt", "updatedAt", device, assigned) VALUES (4, 'robox', 'robot_dog_sr_20004', 'box.json', 'KgJivFmF6gvuFPctih8Mq7uFYLtEN+yAWYypZNI7qy4=', '-----BEGIN PRIVATE KEY-----
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
b45D3WPpAiKJBFdJCJ417e2PUZUCzGs=
-----END PRIVATE KEY-----
', NULL, false, '2019-05-31 21:34:19.038+08', '{}', '2019-05-30 02:28:43.199+08', '2019-05-31 21:34:19.038+08', 'd79b6330-4b5e-4f8f-a5d4-343e702b9c94', NULL);


--
-- Data for Name: Device; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Device" (id, alias, state, "publicKey", fingerprint, "localAddress", "remoteAddress", "defaultUsername", install_uuid, system, platform, "createdAt", "updatedAt", "userId") VALUES ('5df673f2-166a-4600-a5fe-d9d5d82b7790', 'robot_dog_sr_20002', 'offline', '-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAtghZhqX7rUeNxcmLi9Zc
Yu3ISS3AOVOHQhIVUjoyfwkk7549SNpk0Si93uPvzSf73fZSNu8ES4Lixh4eeRbb
YZgb622lF8b41M2hFp05fuIm/yjtGxBZlhBA7JyVyizkwTFo6s0RE6j7VprQ/NDj
6jfUcCWb9Ixxqm7sleCjWdhRnPd7Yw2tTb+g7vQcDdFpw7MRof2Y1IhXXW0EcjK1
6sf6RnsnlO3pzcgjBNdXbBkh/V/3fuNGb2vPN7nEIHADLU9W7sIdoe/IJtBdSRrb
LpICipHqqP2RlUnVbFZknSBL2qFbO9c7d7qL8CorqXQdZgV5kDUMyu3KMyUbBY+B
HtFOlmWhX7iNc9EG8/mXVj71rrIOnVabv9f7yZJXBckFoXm0cHG2vkQLBVNHvr/u
SfApXrSZZF0iVt0FwulnW+u+RhgTb3QpNntYmIKghqoK1IaPE2XePlyp68ucn0Qg
FcvA5xthp5nOGP33zH1yGZ6mYrebJEotVHKZhwCQ7l4HN2088WzjHgwFLqGmCsvv
bTSq0UUZR1ErZBWta+NO9VY/C5UcpvW/PM0Fy/PD9j3UiR2cuU+P2fMsLCu3uEwq
mN2PfJPuE7CQYaSZhjd2mnLL5aEMZeScgWOXyNLaDgRnN686ZgvFEgW4Vu2kMvzN
MpwQ3lY0V9c6+yKsp5wC7HsCAwEAAQ==
-----END PUBLIC KEY-----
', 'SHA256:VsHJgqHO/y5a+igMpPG/ViACyGEeGKa2GRvv2JQhh4k', '10.42.0.1', '117.186.122.46', 'box', 'c295c006-7469-4960-9240-8d94228ce81c', 'ubuntu_18.04', 'n4100', '2019-06-28 11:47:46.168+08', '2020-02-21 07:23:24.821+08', 1);
INSERT INTO public."Device" (id, alias, state, "publicKey", fingerprint, "localAddress", "remoteAddress", "defaultUsername", install_uuid, system, platform, "createdAt", "updatedAt", "userId") VALUES ('bf3c4914-8529-4427-8e90-6cb2aa5d4d3d', 'robot_dog_sr_20003', 'offline', '-----BEGIN PUBLIC KEY-----
MIICCgKCAgEA562IyJhFALOlXuidU90vQpRYNeRZC4VeSYC7yRrXb5HjJ4H1n2Fd
MCD0RD9kKf54bQu3JetswD4QizsHyLrEXM9Rs4npolKvDHLC7/NoB5m5NIbcy/AU
mJQg+3k+sXZuNOmGRIOs+cvGB4ifAtqDNg070/27OUiDgmFEINSqwbPM2GcVSdvN
OmWMoAEuWPhauNLfvc+VeZLpT2r2GeE+WTNVR2uWF9KeS+Sqe8dhk6IInBiFzNky
w2tq8Xf2ksBZ0NuJTRMxc+/M9cZf0QZDtWW91KAuYy7dx08sYT3zfI+e8AI7SFcS
8U0vxXSufJQWddKLlpTsjWDzsD7zd4K1IEHjqke9VuLGkF9TNyE1D5t9XFF2NySE
3DMjYAjYsZuS/WauVkXhQXVSGD6/809A7iMlKi9AMkLn8N79CxOpTkHEcJqRQ25h
zlM7nXBQ8+SjuPBqRRFASsYCDSkM2KlRWJJLiN7L8PGpGqpF4+MULES2hMpdTMFI
MSnjABErpfxLFSJNxSdh483peIGrhPt0yK2samFWYsvxAcom3Rt9RaBruTAfyu1Z
x8TjgBEMXth6lxxpqFnKlfxnm3Pr8q50fe7KR7MVOZkO0OoWEdXZp91uh+hzvtz+
XvlnEuPHFUFsiQx+6mqxoLVmCiWo3QlE1aBJUtXAnnT/V/RqpqiPGPMCAwEAAQ==
-----END RSA PUBLIC KEY-----
', 'SHA256:Me6V8GaAq+7CRs3zxbwjV5gSyUPNUfFqPPq4nytsOlw', '10.1.10.187', '24.23.250.37', 'box', '42ae7f5d-b06f-457d-bfbf-67a8ce0bc9ee', 'ubuntu_18.04', 'n4100', '2019-05-30 03:08:07.13+08', '2020-02-21 07:23:24.821+08', 1);
INSERT INTO public."Device" (id, alias, state, "publicKey", fingerprint, "localAddress", "remoteAddress", "defaultUsername", install_uuid, system, platform, "createdAt", "updatedAt", "userId") VALUES ('d79b6330-4b5e-4f8f-a5d4-343e702b9c94', 'robot_dog_sr_20004', 'offline', '-----BEGIN PUBLIC KEY-----
MIICCgKCAgEA7sbJX4h5uP5bn5LpSXQcealdh94GI2YU1s7v1jSLSSFAudpi3S3r
4qNl5nGxmzMO8hz5Sfga57px8kC8svwLxq+kqPeB9ZNctLNYfuj31b3lfGbJ86Sk
XlimT+DHNEXxBQe8fA/L1Sos1OEySABDUwGKJSqs4MYltO+H/SkypZEfRRvqZ23p
yhu/Q6su+aY5WYpGVUyOdYQxWOB+fIHw/0F4eZ96zsuv1LqLNmbhOgDpdRqJudVy
tul9/MocZlcnL/yBKOfM7sXSNIWLSuzwqvPKwx91vOlADQdoX30C2dz0dbQ4WM59
sWDeRv4Ibo+bHDmw3meoddJg0DIsvRlCAMfZs1KR07n6yyyZjYiG7w/N0Kn/gzRC
OJISKizVqc/odD9oU2YYj8x9YP+VQhQbivxc+dFDTUdlkzqjNMWMPVf/jxsfd7j+
ltSGLiJwZNZkI+1Ki/4kd6wiPt9zA7aiHabBmoi8PqB+rKUblqGiWB5cXxc4lRFi
LAa/jf4TgyeHbatc5a4dSutq9bGl2aHEuuxaU+CbHFtHE15AMX/sCB66LTa3KfpN
LkH8AU5/Fs7070DtbvmNVTaJ4nyz+47Zwt7yA6EF8nQi2gjlea9FZQalad3xMSVP
/oSG9m4Z3SeQdVb8tIxDOlyCG8kGBbbPi5ieXsNh7trFugM0rikr/R8CAwEAAQ==
-----END RSA PUBLIC KEY-----
', 'SHA256:JHa1Ok6R85iAzZwWjRin2MZFk7Hf5bKvcZIUxBkNTTQ', '10.42.0.1', '58.213.230.57', 'box', '04ce741f-9def-4dbb-8605-49ac66806169', 'ubuntu_18.04', 'n4100', '2020-03-05 17:21:48.868+08', '2020-03-25 16:45:33.801+08', 1);
INSERT INTO public."Device" (id, alias, state, "publicKey", fingerprint, "localAddress", "remoteAddress", "defaultUsername", install_uuid, system, platform, "createdAt", "updatedAt", "userId") VALUES ('27bf74b0-4ef0-4e0d-a92d-eb99b9987dea', 'box_dog_sr_50006', 'offline', '-----BEGIN PUBLIC KEY-----
MIICCgKCAgEA0jAyTuqrWxwYkrwVwgl5Omr5lBYFXVHct21WrodhChQM7nZGrbGd
3NTbKpfQBgKqf1v3sB+8HKj9HaE4s4Sdx1MxP+lg0DDTWPNLQNkdWZpKfxfWPt5O
NkgBRLGgT5CUj/uIAU77fuUOrbTyqDJJJHXFmfLEmJ3sEO/NelEqAyt1cXL7I9AC
TwgbCJQSRk0Ai+jlMGSjbK3kyCSqHngA9Lob8F7wPRLvQ9fXWxv7NB8sj/hUCHtS
76Y9KcLkW5WGFnm9l2DYurUkdOPfklUVq3lxih9hrAodfuvpPcG0QOYDdDYTyimd
Nc1n0w7QHLkJ9frDjvxAtq6/aSrbsUM4gAMk2r7PNDw28ZTz3o/GDvCA+9Y+A8Cu
TGG72rPhdPGTYtR42jU+V94EMUCjsEnMnO7c9C1iaq98zpG40TWjpt2M1vJhO5yM
KWvCMUdY1N4lwRx5rblbzelV2p0tyKRUL6manlV9ns8bRrvh6Y4rSbPdGZda+Tlh
BKBRSrN28ofSnSk3Jli5n6R8IFNTuju5yGLulG0SrMiXYuREkeFXzep1Mu2nMCIR
wYyDHXIF5iySgJB6i1/gAN/Nvprum6v6dN47DUEF0/KhhGlrhTvnEAQS4zjrXIAq
3Qf8mNTIaeXTI4pdXGJugFF3h0aRxRrfyJJB5BiUSIEKBD/iHuZFc8UCAwEAAQ==
-----END RSA PUBLIC KEY-----
', 'SHA256:3sv/fqI32e1n214QVs/hJsXKnARMn+SxHgw2hErdHqM', '192.168.28.137', '49.66.176.133', 'turingvideo', '54dfe243-f851-4531-abc2-17f96b5d75df', 'ubuntu_18.04', 'i7-8700', '2019-07-05 10:33:11.833+08', '2020-02-21 07:23:24.821+08', 1);
INSERT INTO public."Device" (id, alias, state, "publicKey", fingerprint, "localAddress", "remoteAddress", "defaultUsername", install_uuid, system, platform, "createdAt", "updatedAt", "userId") VALUES ('8eecdf32-93ca-4a80-b8b6-7e3b875073aa', 'box_dog_sr_50002', 'offline', '-----BEGIN PUBLIC KEY-----
MIICCgKCAgEA36GLqjBJfrjnol30PFuQGxKVFH9MjmslSWBPUhzo+VljhZra2mfL
fMFE8ds2NFVx/kXWnJwAA0G0qOD5N6LR3LaEwAiuEjLwS3fRCQlPbmbCaP1jFRdd
EKaiZrKOp+BVmKdkNG7q40hDWENxrTl6+VD+Ex5kRE2K5ZxEmwJ5WumxxwMyAtt8
9zYkSTAmUZHh38E0rY0TLMnjZji+MZgSaFxSksD6RdaiOC7iqB6qgfE3fP9F69Pf
FUrhnlzGlBT+zuLb6cNUNvKuyJWT4/+2G9hzpaFNgBeYFUXzgIU04I3pFWhO1Ced
8aEjCDUVeAJ6Hw3tUUgdXODiYfgsMOz0HXe2q3bZYI0X4ksFevXJUqTKKqFdWhZZ
uvnB5hq+JbKh8+ASNjeq3hxmeKtskZyb1h8Uiotj0soTJ7NbmzJlDPC9llbQ9Wlj
rn/mFeZHMUdfsUCWnkq4duC2QOnpxU6ZAynUHIFCRQh891WTQbNhTtKBnbZgTewi
CWS/4tJmQ6zloLU5WuP22jU89h9fG6ALAfe2HRnfl32LCUrybZZC9Pucv426xPJQ
IaX7gM8naYrGjeznho1PJZRMCpHgvcoU5VBfyw4WmX3IN2KcSvUM5Dwf2Qtfqa5E
OHO7aJmfKK+heue+geMdLEsZdCmbLNSt4Dc57mg4KifpJrLaKxg1uE8CAwEAAQ==
-----END RSA PUBLIC KEY-----
', 'SHA256:wHNRK0NG+vyDoAN4WUSqXlU4rhGlYfSqb7i1W7k5VWE', '192.168.1.113', '49.71.210.163', 'turingvideo', 'a0578aae-a7a8-4c72-ba66-11d5d1c18a0b', 'ubuntu_18.04', 'i7-8700', '2019-07-05 17:57:06.065+08', '2020-02-21 07:23:24.821+08', 1);


--
-- Data for Name: DeviceUpdate; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."DeviceUpdate" (id, "deviceId", service, "updateConfig", result, "updateId", "createdAt") VALUES (1, '5df673f2-166a-4600-a5fe-d9d5d82b7790', 'robox', '{"service":"slam_server","system":"ubuntu_18.04","platform":"generic","version":"11111","dist":{"id":7,"service":"slam_server","_system":null,"system":"ubuntu_18.04","platform":"generic","version":"11111","level":0,"s3_bucket":"data-for-zeno","s3_key":"dist/slam_server/ubuntu_18.04/generic/11111-1557978070246","createdAt":"2019-05-16T03:41:10.974Z","updatedAt":"2019-05-16T03:41:10.974Z"},"requestedAt":1557978130755,"userId":1}', '{"ec":0,"em":"ok","dm":"ok"}', '1', '2019-05-16 11:42:13.707+08');
INSERT INTO public."DeviceUpdate" (id, "deviceId", service, "updateConfig", result, "updateId", "createdAt") VALUES (2, '5df673f2-166a-4600-a5fe-d9d5d82b7790', 'robox', '{"service":"slam_server","system":"ubuntu_18.04","platform":"generic","version":"11111","dist":{"id":7,"service":"slam_server","_system":null,"system":"ubuntu_18.04","platform":"generic","version":"11111","level":0,"s3_bucket":"data-for-zeno","s3_key":"dist/slam_server/ubuntu_18.04/generic/11111-1557978070246","createdAt":"2019-05-16T03:41:10.974Z","updatedAt":"2019-05-16T03:41:10.974Z"},"requestedAt":1557978218220,"userId":1}', '{"ec":0,"em":"ok","dm":"ok"}', '1', '2019-05-16 11:43:40.666+08');
INSERT INTO public."DeviceUpdate" (id, "deviceId", service, "updateConfig", result, "updateId", "createdAt") VALUES (3, '27bf74b0-4ef0-4e0d-a92d-eb99b9987dea', 'box', '{"service":"box","system":"generic","platform":"generic","version":"0.10.5","dist":{"id":9,"service":"box","_system":null,"system":"generic","platform":"generic","version":"0.10.5","level":0,"s3_bucket":"data-for-zeno","s3_key":"dist/box/generic/generic/0.10.5-1558722332405","createdAt":"2019-05-24T18:25:33.984Z","updatedAt":"2019-05-24T18:25:33.984Z"},"requestedAt":1558723565096,"userId":5}', '{"ec":0,"em":"ok","dm":"ok"}', '5', '2019-05-25 02:46:16.422+08');
INSERT INTO public."DeviceUpdate" (id, "deviceId", service, "updateConfig", result, "updateId", "createdAt") VALUES (4, 'd79b6330-4b5e-4f8f-a5d4-343e702b9c94', 'zeno', '{"service":"robox","system":"generic","platform":"generic","version":"0.11.0pre","dist":{"id":18,"service":"robox","_system":null,"system":"generic","platform":"generic","version":"0.11.0pre","level":1,"s3_bucket":"data-for-zeno","s3_key":"dist/robox/generic/generic/0.11.0pre-1559170105683","createdAt":"2019-05-29T22:48:27.959Z","updatedAt":"2019-05-29T22:48:27.959Z"},"requestedAt":1559170235129,"userId":5}', '{"ec":0,"em":"ok","dm":"ok"}', '5', '2019-05-30 06:50:52.194+08');
INSERT INTO public."DeviceUpdate" (id, "deviceId", service, "updateConfig", result, "updateId", "createdAt") VALUES (5, '5df673f2-166a-4600-a5fe-d9d5d82b7790', 'apk-robot', '{"service":"apk-robot","system":"generic","platform":"generic","version":"0.11.3","dist":{"id":15,"service":"apk-robot","_system":null,"system":"generic","platform":"generic","version":"0.11.3","level":0,"s3_bucket":"data-for-zeno","s3_key":"dist/apk-robot/generic/generic/0.11.3-1558978991617","createdAt":"2019-05-27T17:43:12.351Z","updatedAt":"2019-05-27T17:43:12.351Z"},"requestedAt":1559182262501,"userId":5}', '{"ec":0,"em":"ok","dm":"ok"}', '5', '2019-05-30 10:11:51.207+08');


--
-- Data for Name: Dist; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Dist" (id, service, _system, system, platform, version, level, s3_bucket, s3_key, "createdAt", "updatedAt") VALUES (1, 'robot-launcher', NULL, 'generic', 'generic', '0.1.2', 0, 'data-for-zeno', 'dist/robot-launcher/generic/generic/0.1.2-1558975824758', '2019-05-28 00:50:24.864+08', '2019-05-28 00:50:24.864+08');
INSERT INTO public."Dist" (id, service, _system, system, platform, version, level, s3_bucket, s3_key, "createdAt", "updatedAt") VALUES (2, 'apk-robot', NULL, 'generic', 'generic', '0.11.3', 0, 'data-for-zeno', 'dist/apk-robot/generic/generic/0.11.3-1558978991617', '2019-05-28 01:43:12.351+08', '2019-05-28 01:43:12.351+08');
INSERT INTO public."Dist" (id, service, _system, system, platform, version, level, s3_bucket, s3_key, "createdAt", "updatedAt") VALUES (3, 'robox', NULL, 'generic', 'generic', '0.11.0pre', 1, 'data-for-zeno', 'dist/robox/generic/generic/0.11.0pre-1559170105683', '2019-05-30 06:48:27.959+08', '2019-05-30 06:48:27.959+08');
INSERT INTO public."Dist" (id, service, _system, system, platform, version, level, s3_bucket, s3_key, "createdAt", "updatedAt") VALUES (4, 'guardian', NULL, 'generic', 'generic', '1.2.12-longhu', 0, 'data-for-zeno', 'dist/guardian/generic/generic/1.2.12-longhu-1560848474442', '2019-06-18 17:01:15.402+08', '2019-06-18 17:01:15.402+08');


--
-- Data for Name: Installation; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Installation" (uuid, "createdAt", "updatedAt", oem_uuid) VALUES ('2f07183b-e8e7-4b48-ba6f-eac1e294507e', '2019-05-30 00:55:28.87+08', '2019-05-30 00:55:28.874+08', '0c0b78b8-9e27-4098-b5ea-fc5a10acab57');


--
-- Data for Name: LevelRequirement; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (1, NULL, 'robox', 'latest', 'ubuntu_18.04', 'generic', 0, '0.1.2', '2019-05-30 07:44:05.679+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (2, NULL, 'robox', 'latest', 'generic', 'generic', 0, '0.3.2', '2019-05-30 08:00:41.614+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (3, NULL, 'robox', 'latest', 'generic', 'generic', 1, '0.14.4', '2020-02-04 07:51:34.272+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (4, NULL, 'box', 'min', 'ubuntu_18.04', 'n3450', 0, '1.0.0', '2020-01-17 14:23:12.349+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (5, NULL, 'box', 'latest', 'ubuntu_18.04', 'n3450', 1, '1.2.0', '2020-01-17 14:23:24.381+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (6, NULL, 'apk-robot', 'latest', 'generic', 'generic', 1, '0.3.1rc', '2020-01-18 07:00:05.62+08');
INSERT INTO public."LevelRequirement" (id, _system, service, tag, system, platform, level, version, "updatedAt") VALUES (7, NULL, 'zeno', 'latest', 'generic', 'generic', 1, '0.19.1', '2020-01-18 07:00:05.62+08');


--
-- Data for Name: OEM; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."OEM" (uuid, name, details, "createdAt", "updatedAt", user_id) VALUES ('0c0b78b8-9e27-4098-b5ea-fc5a10acab57', 'turingvideo', '{}', '2018-06-21 06:20:32.799099+08', '2019-05-29 15:51:48.171+08', 1);


--
-- Data for Name: Resource; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Resource" (id, rtype, value, "createdAt", "updatedAt", "deviceId", "userId") VALUES (1, 'ssh-port', '65535', '2019-05-08 18:51:11.265+08', '2019-05-08 18:51:11.265+08', NULL, NULL);


--
-- Data for Name: SystemID; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."SystemID" ("deviceId", "systemId", "updatedAt") VALUES ('5df673f2-166a-4600-a5fe-d9d5d82b7790', 'robot_dog_sr_20002', '2019-05-30 03:11:50.648+08');
INSERT INTO public."SystemID" ("deviceId", "systemId", "updatedAt") VALUES ('bf3c4914-8529-4427-8e90-6cb2aa5d4d3d', 'robot_dog_sr_20003', '2019-05-31 09:39:59.054+08');
INSERT INTO public."SystemID" ("deviceId", "systemId", "updatedAt") VALUES ('d79b6330-4b5e-4f8f-a5d4-343e702b9c94', 'robot_dog_sr_20004', '2019-05-31 21:34:19.041+08');
INSERT INTO public."SystemID" ("deviceId", "systemId", "updatedAt") VALUES ('27bf74b0-4ef0-4e0d-a92d-eb99b9987dea', 'box_dog_sr_50006', '2019-05-30 03:11:50.648+08');
INSERT INTO public."SystemID" ("deviceId", "systemId", "updatedAt") VALUES ('8eecdf32-93ca-4a80-b8b6-7e3b875073aa', 'box_dog_sr_50002', '2019-05-31 09:39:59.054+08');


--
-- Data for Name: UpdateStatus; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."User" (id, username, salt, iterations, pass_hash, admin, "resourceLimit", "resourceCount", "verificationHash", "createdAt", "updatedAt", "deletedAt", "pUserId", permissions) VALUES (1, 'lixiuzhi@turingvideo.net', 'loh6/BnoNLzfenVM1nIhtmwTcz7uBIoCpIXhakd7CzU=', 100000, '1rhxh+r3GFmR3a7lwHOw1lUXzvCXiTPPLG1C6EAPr2WHQ+qZUUKbcUyuZHd/RATYr+t8BBUja8wrjKAJbDcNzAk9PvluqxGw2mDU0iFLSA4TU7WJihOqS8s0L1IZcSl3NXg+QpRY4ZFSIOwPLq3kRIJa5iYSZVNacIoQvHg/u6oMGBZFYFpTLnFBnw1eGflmg0oA80B3uIyGZzXRbrMyZ4Wjvnr9P3KFOuFwvsy6840IK16MJNow5Rmr63GGHpN5ji8ZBAk1g8KE8iU9UKieo4Fu+0RuWWDjP7cuEbQMhyNXz2S/RA58AJ8CPo/sQi/TeBvhB3tQJgMSDtC3M2gR1lks8lyQn+p1U22qXj6ajmddv7es7TcY2hNamqqOtMvUserPECgIpqam1cdPPoAL+u8CLcdYKGZDKHg7//3fLDa1Ba5iELvP1QSCJOExSreUcwozXOtmcY0BpbXl0m8tpJByRFFrzQh9xSepnwQsbnEMeMuEhY+cvBMGMcHKW+E9JlIs/iNuh6vOJbxzO2Ity1cLmaxvQX/FJw0c0MW6/HdWf3zfnsARN7zNYFnUhFfOjFfaHG2KePInkY4F2Ro0f//8a34bk7XAWwyAi0mdwakGpDOCSMZeN0Uqxih8J2+25rhd4V1FVtEB8WgFHRd3oClQ4Jd3R8FTHH7AKzIe0t0=', 1073745920, 10, 2, 'YCJIq/SyWu4MaSw6sL4ung==', '2019-05-08 18:57:34.559+08', '2019-05-24 11:22:50.216+08', NULL, NULL, '{}');


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: Credential_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Credential_id_seq"', 5, true);


--
-- Name: DeviceUpdate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."DeviceUpdate_id_seq"', 6, true);


--
-- Name: Dist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Dist_id_seq"', 5, true);


--
-- Name: LevelRequirement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."LevelRequirement_id_seq"', 8, true);


--
-- Name: Resource_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Resource_id_seq"', 2, true);


--
-- Name: User_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."User_id_seq"', 2, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 2, false);


--
-- Name: Credential Credential_credential_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Credential"
    ADD CONSTRAINT "Credential_credential_id_key" UNIQUE (credential_id);


--
-- Name: Credential Credential_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Credential"
    ADD CONSTRAINT "Credential_pkey" PRIMARY KEY (id);


--
-- Name: DeviceUpdate DeviceUpdate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DeviceUpdate"
    ADD CONSTRAINT "DeviceUpdate_pkey" PRIMARY KEY (id);


--
-- Name: Device Device_alias_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Device"
    ADD CONSTRAINT "Device_alias_key" UNIQUE (alias);


--
-- Name: Device Device_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Device"
    ADD CONSTRAINT "Device_pkey" PRIMARY KEY (id);


--
-- Name: Dist Dist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Dist"
    ADD CONSTRAINT "Dist_pkey" PRIMARY KEY (id);


--
-- Name: Installation Installation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Installation"
    ADD CONSTRAINT "Installation_pkey" PRIMARY KEY (uuid);


--
-- Name: LevelRequirement LevelRequirement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."LevelRequirement"
    ADD CONSTRAINT "LevelRequirement_pkey" PRIMARY KEY (id);


--
-- Name: OEM OEM_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OEM"
    ADD CONSTRAINT "OEM_pkey" PRIMARY KEY (uuid);


--
-- Name: Resource Resource_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Resource"
    ADD CONSTRAINT "Resource_pkey" PRIMARY KEY (id);


--
-- Name: SystemID SystemID_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SystemID"
    ADD CONSTRAINT "SystemID_pkey" PRIMARY KEY ("systemId");


--
-- Name: UpdateStatus UpdateStatus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."UpdateStatus"
    ADD CONSTRAINT "UpdateStatus_pkey" PRIMARY KEY ("deviceId");


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: device_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX device_id ON public."Device" USING btree (id);


--
-- Name: resource_rtype_value; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX resource_rtype_value ON public."Resource" USING btree (rtype, value);


--
-- Name: Credential Credential_assigned_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Credential"
    ADD CONSTRAINT "Credential_assigned_fkey" FOREIGN KEY (assigned) REFERENCES public."OEM"(uuid) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: Credential Credential_device_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Credential"
    ADD CONSTRAINT "Credential_device_fkey" FOREIGN KEY (device) REFERENCES public."Device"(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: Device Device_userId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Device"
    ADD CONSTRAINT "Device_userId_fkey" FOREIGN KEY ("userId") REFERENCES public."User"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Installation Installation_oem_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Installation"
    ADD CONSTRAINT "Installation_oem_uuid_fkey" FOREIGN KEY (oem_uuid) REFERENCES public."OEM"(uuid) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: OEM OEM_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."OEM"
    ADD CONSTRAINT "OEM_user_id_fkey" FOREIGN KEY (user_id) REFERENCES public."User"(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: Resource Resource_deviceId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Resource"
    ADD CONSTRAINT "Resource_deviceId_fkey" FOREIGN KEY ("deviceId") REFERENCES public."Device"(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: Resource Resource_userId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Resource"
    ADD CONSTRAINT "Resource_userId_fkey" FOREIGN KEY ("userId") REFERENCES public."User"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

