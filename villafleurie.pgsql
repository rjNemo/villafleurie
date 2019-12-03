--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO nemausat;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO nemausat;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO nemausat;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO nemausat;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO nemausat;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO nemausat;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO nemausat;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO nemausat;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO nemausat;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO nemausat;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO nemausat;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO nemausat;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO nemausat;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO nemausat;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO nemausat;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO nemausat;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_flatpage; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_flatpage (
    id integer NOT NULL,
    url character varying(100) NOT NULL,
    title character varying(200) NOT NULL,
    content text NOT NULL,
    enable_comments boolean NOT NULL,
    template_name character varying(70) NOT NULL,
    registration_required boolean NOT NULL
);


ALTER TABLE public.django_flatpage OWNER TO nemausat;

--
-- Name: django_flatpage_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_flatpage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_flatpage_id_seq OWNER TO nemausat;

--
-- Name: django_flatpage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_flatpage_id_seq OWNED BY public.django_flatpage.id;


--
-- Name: django_flatpage_sites; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_flatpage_sites (
    id integer NOT NULL,
    flatpage_id integer NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.django_flatpage_sites OWNER TO nemausat;

--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_flatpage_sites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_flatpage_sites_id_seq OWNER TO nemausat;

--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_flatpage_sites_id_seq OWNED BY public.django_flatpage_sites.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO nemausat;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO nemausat;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO nemausat;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO nemausat;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO nemausat;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: rental_guest; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_guest (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(254) NOT NULL,
    phone character varying(128) NOT NULL
);


ALTER TABLE public.rental_guest OWNER TO nemausat;

--
-- Name: rental_guest_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_guest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_guest_id_seq OWNER TO nemausat;

--
-- Name: rental_guest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_guest_id_seq OWNED BY public.rental_guest.id;


--
-- Name: rental_image; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_image (
    id integer NOT NULL,
    img character varying(100),
    alt character varying(100) NOT NULL
);


ALTER TABLE public.rental_image OWNER TO nemausat;

--
-- Name: rental_image_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_image_id_seq OWNER TO nemausat;

--
-- Name: rental_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_image_id_seq OWNED BY public.rental_image.id;


--
-- Name: rental_place; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_place (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    description text NOT NULL,
    tagline character varying(100) NOT NULL,
    price numeric(6,2),
    subname character varying(100) NOT NULL,
    beds integer,
    max_occupation integer,
    surface integer,
    info text NOT NULL,
    thumbnail_id integer
);


ALTER TABLE public.rental_place OWNER TO nemausat;

--
-- Name: rental_place_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_place_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_place_id_seq OWNER TO nemausat;

--
-- Name: rental_place_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_place_id_seq OWNED BY public.rental_place.id;


--
-- Name: rental_place_images; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_place_images (
    id integer NOT NULL,
    place_id integer NOT NULL,
    image_id integer NOT NULL
);


ALTER TABLE public.rental_place_images OWNER TO nemausat;

--
-- Name: rental_place_images_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_place_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_place_images_id_seq OWNER TO nemausat;

--
-- Name: rental_place_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_place_images_id_seq OWNED BY public.rental_place_images.id;


--
-- Name: rental_reservation; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_reservation (
    id integer NOT NULL,
    guest_id integer NOT NULL,
    place_id integer NOT NULL,
    message text NOT NULL,
    "end" date NOT NULL,
    start date NOT NULL,
    price numeric(6,2)
);


ALTER TABLE public.rental_reservation OWNER TO nemausat;

--
-- Name: rental_reservation_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_reservation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_reservation_id_seq OWNER TO nemausat;

--
-- Name: rental_reservation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_reservation_id_seq OWNED BY public.rental_reservation.id;


--
-- Name: rental_testimonial; Type: TABLE; Schema: public; Owner: nemausat
--

CREATE TABLE public.rental_testimonial (
    id integer NOT NULL,
    author character varying(100) NOT NULL,
    text text NOT NULL,
    reservation_id integer,
    guest_id integer,
    picture character varying(100),
    link character varying(200)
);


ALTER TABLE public.rental_testimonial OWNER TO nemausat;

--
-- Name: rental_testimonial_id_seq; Type: SEQUENCE; Schema: public; Owner: nemausat
--

CREATE SEQUENCE public.rental_testimonial_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rental_testimonial_id_seq OWNER TO nemausat;

--
-- Name: rental_testimonial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nemausat
--

ALTER SEQUENCE public.rental_testimonial_id_seq OWNED BY public.rental_testimonial.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_flatpage id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage ALTER COLUMN id SET DEFAULT nextval('public.django_flatpage_id_seq'::regclass);


--
-- Name: django_flatpage_sites id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage_sites ALTER COLUMN id SET DEFAULT nextval('public.django_flatpage_sites_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: rental_guest id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_guest ALTER COLUMN id SET DEFAULT nextval('public.rental_guest_id_seq'::regclass);


--
-- Name: rental_image id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_image ALTER COLUMN id SET DEFAULT nextval('public.rental_image_id_seq'::regclass);


--
-- Name: rental_place id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place ALTER COLUMN id SET DEFAULT nextval('public.rental_place_id_seq'::regclass);


--
-- Name: rental_place_images id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place_images ALTER COLUMN id SET DEFAULT nextval('public.rental_place_images_id_seq'::regclass);


--
-- Name: rental_reservation id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_reservation ALTER COLUMN id SET DEFAULT nextval('public.rental_reservation_id_seq'::regclass);


--
-- Name: rental_testimonial id; Type: DEFAULT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial ALTER COLUMN id SET DEFAULT nextval('public.rental_testimonial_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add Voyageur	7	add_guest
26	Can change Voyageur	7	change_guest
27	Can delete Voyageur	7	delete_guest
28	Can view Voyageur	7	view_guest
29	Can add Appartement	8	add_place
30	Can change Appartement	8	change_place
31	Can delete Appartement	8	delete_place
32	Can view Appartement	8	view_place
33	Can add Réservation	9	add_reservation
34	Can change Réservation	9	change_reservation
35	Can delete Réservation	9	delete_reservation
36	Can view Réservation	9	view_reservation
37	Can add Témoignage	10	add_testimonial
38	Can change Témoignage	10	change_testimonial
39	Can delete Témoignage	10	delete_testimonial
40	Can view Témoignage	10	view_testimonial
41	Can add site	11	add_site
42	Can change site	11	change_site
43	Can delete site	11	delete_site
44	Can view site	11	view_site
45	Can add flat page	12	add_flatpage
46	Can change flat page	12	change_flatpage
47	Can delete flat page	12	delete_flatpage
48	Can view flat page	12	view_flatpage
49	Can add image	13	add_image
50	Can change image	13	change_image
51	Can delete image	13	delete_image
52	Can view image	13	view_image
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$FUvMBlxIZy6y$HmwSAxQAdPaOve3XwCYfDx/3Oklh2WtG2QJewPcrO+s=	2019-12-03 13:22:52.850538+01	t	admin	Ruidy	Nemausat	location.villafleurie@gmail.com	t	t	2019-11-06 16:35:14+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
1	1	32
2	1	33
3	1	34
4	1	35
5	1	36
6	1	37
7	1	38
8	1	39
9	1	40
10	1	25
11	1	26
12	1	27
13	1	28
14	1	29
15	1	30
16	1	31
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-11-06 16:39:43.062071+01	1	admin	2	[{"changed": {"fields": ["user_permissions"]}}]	4	1
2	2019-11-06 16:40:27.784357+01	1	admin	2	[{"changed": {"fields": ["first_name", "last_name"]}}]	4	1
3	2019-11-06 16:44:15.299585+01	1	T2	2	[{"changed": {"fields": ["description", "subname", "tagline"]}}]	8	1
4	2019-11-06 16:45:17.940238+01	2	T3	1	[{"added": {}}]	8	1
5	2019-11-06 16:45:24.591962+01	1	T2	2	[{"changed": {"fields": ["tagline"]}}]	8	1
6	2019-11-06 19:49:44.302744+01	1	/contact/ -- Contactez-nous	1	[{"added": {}}]	12	1
7	2019-11-06 19:54:04.789852+01	2	localhost:8000	1	[{"added": {}}]	11	1
8	2019-11-06 19:54:13.717173+01	1	/contact/ -- Contactez-nous	2	[{"changed": {"fields": ["sites"]}}]	12	1
9	2019-11-06 19:55:41.420317+01	1	/contact/ -- Contactez-nous	2	[]	12	1
10	2019-11-06 19:57:21.602461+01	2	/contact_/ -- Contactez-nous	1	[{"added": {}}]	12	1
11	2019-11-06 20:00:07.42598+01	2	/contact_/ -- Contactez-nous	2	[]	12	1
12	2019-11-06 20:10:22.216488+01	1	/contact/ -- Contactez-nous	3		12	1
13	2019-11-06 20:10:27.313039+01	2	/contact_/ -- Contactez-nous	3		12	1
14	2019-11-07 11:32:27.20656+01	1	T2	2	[{"changed": {"fields": ["surface", "beds", "max_occupation"]}}]	8	1
15	2019-11-07 11:32:47.513132+01	2	T3	2	[{"changed": {"fields": ["description", "surface", "beds", "max_occupation"]}}]	8	1
16	2019-11-07 11:46:45.830996+01	2	T3	2	[]	8	1
17	2019-11-07 11:51:59.015395+01	1	T2	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
18	2019-11-07 11:54:41.90995+01	1	T2	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
19	2019-11-07 11:58:26.218543+01	1	T2	2	[{"changed": {"fields": ["description"]}}]	8	1
20	2019-11-07 12:03:00.504809+01	1	T2	2	[{"changed": {"fields": ["description"]}}]	8	1
21	2019-11-07 12:07:42.210109+01	2	T3	2	[{"changed": {"fields": ["description"]}}]	8	1
22	2019-11-07 12:11:27.750187+01	2	T3	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
23	2019-11-07 12:11:30.163063+01	1	T2	2	[{"changed": {"fields": ["description"]}}]	8	1
24	2019-11-07 12:13:18.374504+01	1	T2	2	[{"changed": {"fields": ["description"]}}]	8	1
25	2019-11-07 12:13:25.987552+01	2	T3	2	[{"changed": {"fields": ["description"]}}]	8	1
26	2019-11-07 12:14:56.161642+01	1	T2	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
27	2019-11-07 12:15:18.608399+01	2	T3	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
28	2019-11-07 14:49:42.550211+01	1	Réservation du T3 par djibril Cissé	3		9	1
29	2019-11-07 15:04:29.927468+01	3	Réservation du T2 par mathias	3		9	1
30	2019-11-07 15:04:29.928464+01	2	Réservation du T3 par djibril Cissé	3		9	1
31	2019-11-07 22:16:20.23624+01	1	ENDOU Tatsuya	1	[{"added": {}}]	10	1
32	2019-11-07 22:17:26.573563+01	1	ENDOU Tatsuya	2	[]	10	1
33	2019-11-07 23:16:04.21013+01	1	ENDOU Tatsuya	2	[{"changed": {"fields": ["link"]}}]	10	1
34	2019-11-07 23:23:46.189984+01	1	ENDOU Tatsuya	2	[{"changed": {"fields": ["picture"]}}]	10	1
35	2019-11-07 23:23:55.099694+01	1	ENDOU Tatsuya	2	[{"changed": {"fields": ["picture"]}}]	10	1
36	2019-11-10 19:07:03.849863+01	1	T2	2	[{"changed": {"fields": ["pictures"]}}]	8	1
37	2019-11-10 19:16:09.876949+01	1	villafleurie T2 salon	1	[{"added": {}}]	13	1
38	2019-11-10 19:16:19.635647+01	2	vvillafleurie T2 salon	1	[{"added": {}}]	13	1
39	2019-11-10 19:16:35.212857+01	3	villafleurie T2 sallle de bain	1	[{"added": {}}]	13	1
40	2019-11-10 19:18:09.833505+01	1	villafleurie T2 salon	2	[{"changed": {"fields": ["place"]}}]	13	1
41	2019-11-10 19:18:18.84909+01	3	villafleurie T2 sallle de bain	2	[{"changed": {"fields": ["place"]}}]	13	1
42	2019-11-10 19:18:26.350055+01	2	vvillafleurie T2 salon	2	[{"changed": {"fields": ["place"]}}]	13	1
43	2019-11-10 19:18:29.103516+01	2	vvillafleurie T2 salon	2	[]	13	1
44	2019-11-10 19:18:47.107245+01	4	villafleurie T2 chambre	1	[{"added": {}}]	13	1
45	2019-11-10 19:18:56.213973+01	5	villafleurie T2 chambre	1	[{"added": {}}]	13	1
46	2019-11-10 19:19:13.030473+01	6	villafleurie T2 cuisine	1	[{"added": {}}]	13	1
47	2019-11-10 19:19:24.244299+01	7	villafleurie T2 terrasse	1	[{"added": {}}]	13	1
48	2019-11-10 19:42:28.230913+01	7	villafleurie T2 terrasse	2	[{"changed": {"fields": ["place"]}}]	13	1
49	2019-11-10 19:42:36.123699+01	6	villafleurie T2 cuisine	2	[{"changed": {"fields": ["place"]}}]	13	1
50	2019-11-10 19:42:40.409982+01	5	villafleurie T2 chambre	2	[{"changed": {"fields": ["place"]}}]	13	1
51	2019-11-10 19:42:45.609566+01	5	villafleurie T2 chambre	2	[]	13	1
52	2019-11-10 19:42:49.316262+01	4	villafleurie T2 chambre	2	[{"changed": {"fields": ["place"]}}]	13	1
53	2019-11-10 19:42:55.228264+01	3	villafleurie T2 sallle de bain	2	[{"changed": {"fields": ["place"]}}]	13	1
54	2019-11-10 19:43:23.515447+01	3	villafleurie T2 sallle de bain	2	[]	13	1
55	2019-11-10 19:43:27.560107+01	2	vvillafleurie T2 salon	2	[{"changed": {"fields": ["place"]}}]	13	1
56	2019-11-10 19:43:30.910615+01	1	villafleurie T2 salon	2	[{"changed": {"fields": ["place"]}}]	13	1
57	2019-11-10 20:21:44.217597+01	1	T2	2	[{"changed": {"fields": ["info"]}}]	8	1
58	2019-11-10 20:23:57.447431+01	1	T2	2	[{"changed": {"fields": ["description"]}}]	8	1
59	2019-11-10 20:33:09.478079+01	2	T3	2	[{"changed": {"fields": ["description", "info"]}}]	8	1
60	2019-11-10 20:33:40.164184+01	2	T3	2	[{"changed": {"fields": ["description"]}}]	8	1
61	2019-11-10 20:41:05.017763+01	8	villafleurie T3 salon	1	[{"added": {}}]	13	1
62	2019-11-10 20:41:23.212517+01	9	villafleurie T3 cuisine	1	[{"added": {}}]	13	1
63	2019-11-10 20:41:36.377396+01	10	villafleurie T3 chambre	1	[{"added": {}}]	13	1
64	2019-11-11 09:56:48.594984+01	1	T2	2	[{"changed": {"fields": ["thumbnail", "images"]}}]	8	1
65	2019-11-11 09:57:07.191731+01	2	T3	2	[{"changed": {"fields": ["thumbnail", "images"]}}]	8	1
66	2019-11-11 10:01:20.176581+01	1	T2	2	[{"changed": {"fields": ["thumbnail"]}}]	8	1
67	2019-11-11 10:31:05.439903+01	1	Nell	2	[{"changed": {"fields": ["author", "text", "picture", "guest"]}}]	10	1
68	2019-11-11 10:31:11.880184+01	1	Nell	2	[{"changed": {"fields": ["picture"]}}]	10	1
69	2019-11-11 10:32:39.641913+01	2	Laurence	1	[{"added": {}}]	10	1
70	2019-11-11 10:35:59.288836+01	3	Thomas	1	[{"added": {}}]	10	1
71	2019-11-11 12:02:19.846461+01	24	Réservation du T3 par Ruidy Nemausat	3		9	1
72	2019-11-11 12:02:19.849346+01	4	Réservation du T2 par Jean	3		9	1
73	2019-11-11 12:02:27.62568+01	24	fred	3		7	1
74	2019-11-11 12:02:27.628312+01	9	Jean	3		7	1
75	2019-11-11 12:02:27.629386+01	8	mathias	3		7	1
76	2019-11-11 12:02:27.630985+01	7	djibril Cissé	3		7	1
77	2019-11-11 12:02:27.633855+01	5	Nilka	3		7	1
78	2019-11-11 12:02:27.634982+01	3	Ruidy Nemausat	3		7	1
79	2019-11-11 12:08:36.294003+01	45	Réservation du T3 par Ruidy Nemausat	3		9	1
80	2019-11-11 12:08:36.297431+01	43	Réservation du T2 par Ruidy Nemausat	3		9	1
81	2019-11-11 12:12:21.260176+01	47	Réservation du T2 par Nilka	3		9	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	rental	guest
8	rental	place
9	rental	reservation
10	rental	testimonial
11	sites	site
12	flatpages	flatpage
13	rental	image
\.


--
-- Data for Name: django_flatpage; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_flatpage (id, url, title, content, enable_comments, template_name, registration_required) FROM stdin;
\.


--
-- Data for Name: django_flatpage_sites; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_flatpage_sites (id, flatpage_id, site_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-11-06 12:50:21.7169+01
2	auth	0001_initial	2019-11-06 12:50:21.770845+01
3	admin	0001_initial	2019-11-06 12:50:21.809378+01
4	admin	0002_logentry_remove_auto_add	2019-11-06 12:50:21.823969+01
5	admin	0003_logentry_add_action_flag_choices	2019-11-06 12:50:21.837085+01
6	contenttypes	0002_remove_content_type_name	2019-11-06 12:50:21.858848+01
7	auth	0002_alter_permission_name_max_length	2019-11-06 12:50:21.867999+01
8	auth	0003_alter_user_email_max_length	2019-11-06 12:50:21.87574+01
9	auth	0004_alter_user_username_opts	2019-11-06 12:50:21.887716+01
10	auth	0005_alter_user_last_login_null	2019-11-06 12:50:21.897412+01
11	auth	0006_require_contenttypes_0002	2019-11-06 12:50:21.900186+01
12	auth	0007_alter_validators_add_error_messages	2019-11-06 12:50:21.917921+01
13	auth	0008_alter_user_username_max_length	2019-11-06 12:50:21.93388+01
14	auth	0009_alter_user_last_name_max_length	2019-11-06 12:50:21.942184+01
15	auth	0010_alter_group_name_max_length	2019-11-06 12:50:21.953744+01
16	auth	0011_update_proxy_permissions	2019-11-06 12:50:21.961307+01
17	rental	0001_initial	2019-11-06 12:50:21.994702+01
18	sessions	0001_initial	2019-11-06 12:50:22.016897+01
19	rental	0002_auto_20191106_1542	2019-11-06 16:43:04.044004+01
20	sites	0001_initial	2019-11-06 19:33:06.421357+01
21	flatpages	0001_initial	2019-11-06 19:33:06.433684+01
22	sites	0002_alter_domain_unique	2019-11-06 19:33:06.453708+01
23	rental	0003_auto_20191107_1031	2019-11-07 11:31:51.761014+01
24	rental	0004_place_info	2019-11-07 11:46:34.427152+01
25	rental	0005_reservation_message	2019-11-07 14:49:17.443558+01
26	rental	0006_auto_20191107_2114	2019-11-07 22:14:52.607102+01
27	rental	0007_auto_20191107_2116	2019-11-07 22:16:14.193072+01
28	rental	0008_auto_20191107_2214	2019-11-07 23:14:10.331227+01
29	rental	0009_auto_20191107_2220	2019-11-07 23:20:53.338651+01
30	rental	0010_auto_20191107_2221	2019-11-07 23:22:00.3625+01
31	rental	0011_auto_20191107_2223	2019-11-07 23:23:17.225716+01
32	rental	0012_auto_20191110_1814	2019-11-10 19:14:56.354784+01
33	rental	0013_auto_20191110_1817	2019-11-10 19:17:46.478345+01
34	rental	0014_auto_20191110_1822	2019-11-10 19:22:31.152069+01
35	rental	0015_auto_20191110_1825	2019-11-10 19:25:23.249636+01
36	rental	0016_auto_20191110_1826	2019-11-10 19:26:26.944491+01
37	rental	0017_auto_20191111_0855	2019-11-11 09:55:41.245508+01
38	rental	0018_auto_20191111_0912	2019-11-11 10:12:51.65767+01
39	rental	0019_auto_20191111_1020	2019-11-11 11:20:07.063528+01
40	rental	0020_auto_20191111_1038	2019-11-11 11:38:10.633306+01
41	rental	0021_auto_20191111_1112	2019-11-11 12:12:03.089484+01
42	rental	0022_auto_20191111_1211	2019-11-11 13:11:57.421877+01
43	rental	0023_reservation_quotation	2019-12-03 13:22:30.586657+01
44	rental	0024_auto_20191203_1227	2019-12-03 13:27:38.22714+01
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
cfdjrvyssfllbjdxeep6a6ceyfia1ils	YjEwNmVhMzBlZTI5NDhiMWQyZDQ4YjkxZjFjMDQ0NWU2ZDc1NjkzZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjNhMTFhZWVmY2ViNjFiMGZjYjZhOGU1Yzg2NjBjMzA3MTAwZmQwIn0=	2019-11-20 16:35:48.543646+01
5kwgp6mr5umgt78man1s629lokcyagcp	YjEwNmVhMzBlZTI5NDhiMWQyZDQ4YjkxZjFjMDQ0NWU2ZDc1NjkzZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjNhMTFhZWVmY2ViNjFiMGZjYjZhOGU1Yzg2NjBjMzA3MTAwZmQwIn0=	2019-12-17 13:22:52.854255+01
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
2	localhost:8000	dev
\.


--
-- Data for Name: rental_guest; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_guest (id, name, email, phone) FROM stdin;
28	Ruidy Nemausat	ruidy.nemausat@gmail.com	
29	Nilka	nilka.gordien@gmail.com	
30	andre	andre@mail.fr	
31	bobi	bobi@maiil.fr	
33	charles	ch@mail.com	
34	david	d@mail.com	
36	Nilka	nemo@mail.com	
\.


--
-- Data for Name: rental_image; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_image (id, img, alt) FROM stdin;
7	img/villafleurie_t2_terrasse.jpg	villafleurie T2 terrasse
6	img/villafleurie_t2_cuisine.jpg	villafleurie T2 cuisine
5	img/villafleurie_t2_chambre_2.jpg	villafleurie T2 chambre
4	img/villafleurie_t2_chambre.jpg	villafleurie T2 chambre
3	img/villafleurie_t2_sallle_de_bain.jpg	villafleurie T2 sallle de bain
2	img/villafleurie_t2_salon_2.jpg	vvillafleurie T2 salon
1	img/villafleurie_t2_salon_1_wl81yXI.jpg	villafleurie T2 salon
8	img/villafleurie_t3_salon.jpg	villafleurie T3 salon
9	img/villafleurie_t3_cuisine.jpg	villafleurie T3 cuisine
10	img/villafleurie_t3_chambre.jpg	villafleurie T3 chambre
\.


--
-- Data for Name: rental_place; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_place (id, name, description, tagline, price, subname, beds, max_occupation, surface, info, thumbnail_id) FROM stdin;
1	T2	<strong>Réservez</strong> votre séjour au coeur de la station balnéaire du Gosier à deux pas des plages à un tarif sympa : <strong><a href="#reservation"> à partir de 50 €</a>.</strong></p>\r\n\r\n<p style="text-align: justify;">Nous vous proposons ce <strong>cosy T2</strong> pour <strong>1 à 2 personnes (et 1 bébé)</strong>. Il est idéalement situé dans le bourg du Gosier. Ainsi profitez des <strong>plages et activités</strong> de la dynamique et chaleureuse ville du Gosier tout en bénéficiant du <strong>calme</strong> nécessaire à vos séances de <i>farniente.</i></p>\r\n\r\n<p style="text-align: justify;"><strong>Excellent rapport qualité/prix</strong> et une situation géographique qui convient parfaitement aux <strong>séjours touristiques et d’affaires</strong>.\r\n<br />Possibilité de location mensuelle de moins de 4 mois à<strong> tarifs dégressifs</strong>. \r\n<br/><a href="#tarifs">Voir tarifs ci-dessous.</a></p>\r\n\r\n<p style="text-align: justify;">Le T2 est doté d’une place de <strong>parking privé</strong>, une terrasse avec stores et d’un coin jardin. Il est naturellement ventilé et profite d'un ensoleillement continu du matin au soir.</p>\r\n\r\n<div class="row section-t3">\r\n                <div class="col-sm-12">\r\n                  <div class="title-box-d">\r\n                    <h3 class="title-d">Équipements</h3>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n              <div class="amenities-list color-text-a">\r\n                <ul class="list-a no-margin">\r\n                  <li>Climatisation (silencieuse)</li>\r\n                  <li>Lit double dans la chambre</li>\r\n                  <li>Confortable canapé-lit dans le salon</li>\r\n                  <li>Lit parapluie disponible pour un bébé (sur demande)</li>\r\n                  <li>Cuisine équipée avec table à manger, gazinière, micro-onde, bouilloire, réfrigérateur et vaisselle fournie</li>\r\n                  <li>Salle de douche et WC indépendants</li>\r\n                  <li>Parking</li>\r\n                  <li>Draps et serviettes de bain (selon durée du séjour)</li>\r\n                  <li>Fer et table à repasser</li>\r\n                  <li>TV par satellite</li>\r\n                  <li>Internet via WIFI</li>\r\n                </ul>\r\n              </div>	Envie d'un petit cocon ?	50.00	Cosy	1	2	65	<div class="row section-t3">\r\n                <div class="col-sm-12">\r\n                  <div class="title-box-d">\r\n                    <h3 class="title-d">Tarifs</h3>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n              <div class="amenities-list color-text-a">\r\n                <ul class="list-b no-margin">\r\n                  <li>55 € la nuit</li>\r\n                  <li>350 € la semaine (au lieu de 385 €)</li>\r\n                  <li>645 € pour 2 semaines (au lieu de 825 €)</li>\r\n                  <li>960 € le mois (au lieu de 1650 €)</li>\r\n                </ul>\r\n              </div>\r\n\r\n<p>Vous êtes intéressés ? Vérifiez les disponibilités ci-contre.  <strong><a href="#reservation">Réservez maintenant !</a></strong></p>\r\n<p>*<em>Les tarifs ci-dessus concernent une réservation pour <strong>2 personnes</strong>. Prévoir un coût additionnel de <strong>15 € par personnes</strong> au-delà de 2 personnes.  Les enfants bénéficient d'un tarif préférentiel, <strong>10 €</strong> seulement par <strong>enfant de moins de 10 ans</strong> et <strong>5 €</strong> pour les bébés de <strong>moins de 3 ans</strong>.</em></p>\r\n<p style="text-align: center;">Besoin de <strong>plus d'espace</strong> ? Nous avons également un <strong><a href="/T3/">T3</a></strong> à votre disposition !</p>	1
2	T3	<strong>Réservez</strong> votre séjour au coeur de la station balnéaire du Gosier à deux pas des plages à un tarif sympa : <strong>à partir de <a href="#reservation">60 €</a>.</strong></p>\r\n\r\n<p style="text-align: justify;">Nous vous proposons ce <strong>spacieux T3</strong> pour <strong>1 à 4 personnes</strong>. Il est idéalement situé dans le bourg du Gosier. Ainsi profitez des <strong>plages et activités</strong> de la dynamique et chaleureuse ville du Gosier tout en bénéficiant du <strong>calme</strong> nécessaire à vos séances de <i>farniente.</i></p>\r\n\r\n<p style="text-align: justify;"><strong>Excellent rapport qualité/prix</strong> et une situation géographique qui convient parfaitement aux <strong>séjours touristiques et d’affaires</strong>.\r\n<br />Possibilité de location mensuelle de moins de 4 mois à<strong> tarifs dégressifs</strong>. \r\n<br/><a href="#tarifs">Voir tarifs ci-dessous.</a></p>\r\n\r\n<p style="text-align: justify;">Le T3 est doté d’une place de <strong>parking privé</strong>, une terrasse avec stores et d’un coin jardin. Il est naturellement ventilé et profite d'un ensoleillement continu du matin au soir.</p>\r\n\r\n<div class="row section-t3">\r\n                <div class="col-sm-12">\r\n                  <div class="title-box-d">\r\n                    <h3 class="title-d">Équipements</h3>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n              <div class="amenities-list color-text-a">\r\n                <ul class="list-a no-margin">\r\n                  <li>Climatisation (silencieuse)</li>\r\n                  <li>Lit double dans chacune des chambres</li>\r\n                  <li>Confortable canapé-lit dans le salon</li>\r\n                  <li>Lit parapluie disponible pour un bébé (sur demande)</li>\r\n                  <li>Bureau dans une chambre</li>\r\n                  <li>Cuisine équipée avec table à manger, gazinière, micro-onde, bouilloire, réfrigérateur et vaisselle fournie</li>\r\n                  <li>Salle de douche et WC indépendants</li>\r\n                  <li>Parking</li>\r\n                  <li>Draps et serviettes de bain (selon durée du séjour)</li>\r\n                  <li>Fer et table à repasser</li>\r\n                  <li>TV par satellite</li>\r\n                  <li>Internet via WIFI</li>\r\n                </ul>\r\n              </div>	Besoin de plus d’espace ?	60.00	Spacieux	2	4	65	<div class="row section-t3">\r\n                <div class="col-sm-12">\r\n                  <div class="title-box-d">\r\n                    <h3 class="title-d">Tarifs</h3>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n              <div class="amenities-list color-text-a">\r\n                <ul class="list-b no-margin">\r\n                  <li>60 € la nuit</li>\r\n<li>385 € la semaine (au lieu de 420 €)</li>\r\n<li>705 € pour 2 semaines (au lieu de 900 €)</li>\r\n<li>1050 € le mois (au lieu de 1800 €)</li>\r\n                </ul>\r\n              </div>\r\n\r\n<p>Vous êtes intéressés ? Vérifiez les disponibilités ci-contre.  <strong><a href="#reservation">Réservez maintenant !</a></strong></p>\r\n<p><em>La législation nous impose de collecter des frais de séjour s'élevant à 1,5 € par personne et par jour.</em></p>\r\n<p>*<em>Les tarifs ci-dessus concernent une réservation pour <strong>2 personnes</strong>. Prévoir un coût additionnel de <strong>15 € par personnes</strong> au-delà de 2 personnes.  Les enfants bénéficient d'un tarif préférentiel, </em><em><strong>10 €</strong> seulement par <strong>enfant de moins de 10 ans</strong> et <strong>5 €</strong> pour les bébés de <strong>moins de 3 ans</strong></em></p>\r\n<p> </p>\r\n<p style="text-align: center;">À la recherche d'un <strong>petit nid douillet</strong> ? Nous avons également un <strong><a href="/T2/">T2</a> </strong>à votre disposition !</p>	10
\.


--
-- Data for Name: rental_place_images; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_place_images (id, place_id, image_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	2	3
9	2	6
10	2	7
11	2	8
12	2	9
13	2	10
\.


--
-- Data for Name: rental_reservation; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_reservation (id, guest_id, place_id, message, "end", start, price) FROM stdin;
48	30	2	vyons	2019-12-12	2019-11-11	\N
49	30	1	bien sur	2019-12-12	2019-11-11	\N
50	31	1	VOila ce que je pense …	2019-12-12	2019-11-11	\N
52	33	2	Test 3	2019-12-12	2019-11-11	\N
53	34	1	deuxiemment	2019-12-12	2019-11-11	\N
55	28	1	rerer	2019-12-12	2019-11-11	\N
56	28	1	rerer	2019-12-12	2019-11-11	\N
57	28	1	Test	2019-11-12	2019-11-11	\N
58	36	1	retest	2019-11-12	2019-11-11	50.00
59	36	1	retest	2019-11-12	2019-11-11	50.00
60	36	1	retest	2019-11-12	2019-11-11	50.00
61	28	1	test	2020-12-12	2020-11-11	\N
\.


--
-- Data for Name: rental_testimonial; Type: TABLE DATA; Schema: public; Owner: nemausat
--

COPY public.rental_testimonial (id, author, text, reservation_id, guest_id, picture, link) FROM stdin;
1	Nell	Nilka and her family ensured we had an amazing stay, picking us up from the airport and dropping us off, giving us tips and ideas of things to do, helping us with everything we needed. The place is light filled, spacious, clean, and all the amenities worked well. The location is great, anything you could need within Le Gosier is within a ten minute walk including shops, a supermarket, a park, the beach, restaurants, bars, and more. If you want to go further, there is a bus stop literally at the top of the street, where you can get to Pointe-à-Pitre within 20 minutes, and many other places very easily. We had a lovely time!	\N	\N	img/b871ce71-2e80-4da1-be7c-b1d5a1374cef.jpg	https://docs.djangoproject.com/fr/2.2/ref/models/fields/#urlfield
2	Laurence	Location très agréable et bien équipée au Gosier. Notre séjour n’a duré qu’une nuit mais nous avons pu apprécier la gentillesse et la disponibilité de nos hôtes. Nous avons aussi beaucoup apprécié les transferts depuis l’aéroport et vers la gare maritime qu’ils nous ont proposé cela nous a rendu un grand service ! Merci aussi pour toutes les explications !	\N	\N	img/original.jpg	\N
3	Thomas	Superbe séjour chez Jacques et Hélène, emplacement au top près des commerces et de la plage de la Datcha (10 grosses minutes à pied). A noter la présence d’un lit parapluie et d’une chaise pour bébé ce qui est un sacré plus !	\N	\N	img/a8cb2ffc-451e-4444-a60b-d8f35668873b.jpg	\N
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 16, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 81, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_flatpage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_flatpage_id_seq', 2, true);


--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_flatpage_sites_id_seq', 3, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 44, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.django_site_id_seq', 2, true);


--
-- Name: rental_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_guest_id_seq', 36, true);


--
-- Name: rental_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_image_id_seq', 10, true);


--
-- Name: rental_place_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_place_id_seq', 2, true);


--
-- Name: rental_place_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_place_images_id_seq', 13, true);


--
-- Name: rental_reservation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_reservation_id_seq', 61, true);


--
-- Name: rental_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nemausat
--

SELECT pg_catalog.setval('public.rental_testimonial_id_seq', 3, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_flatpage django_flatpage_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage
    ADD CONSTRAINT django_flatpage_pkey PRIMARY KEY (id);


--
-- Name: django_flatpage_sites django_flatpage_sites_flatpage_id_site_id_0d29d9d1_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_flatpage_id_site_id_0d29d9d1_uniq UNIQUE (flatpage_id, site_id);


--
-- Name: django_flatpage_sites django_flatpage_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: rental_guest rental_guest_email_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_guest
    ADD CONSTRAINT rental_guest_email_key UNIQUE (email);


--
-- Name: rental_guest rental_guest_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_guest
    ADD CONSTRAINT rental_guest_pkey PRIMARY KEY (id);


--
-- Name: rental_image rental_image_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_image
    ADD CONSTRAINT rental_image_pkey PRIMARY KEY (id);


--
-- Name: rental_place_images rental_place_images_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place_images
    ADD CONSTRAINT rental_place_images_pkey PRIMARY KEY (id);


--
-- Name: rental_place_images rental_place_images_place_id_image_id_2ce6da5a_uniq; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place_images
    ADD CONSTRAINT rental_place_images_place_id_image_id_2ce6da5a_uniq UNIQUE (place_id, image_id);


--
-- Name: rental_place rental_place_name_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place
    ADD CONSTRAINT rental_place_name_key UNIQUE (name);


--
-- Name: rental_place rental_place_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place
    ADD CONSTRAINT rental_place_pkey PRIMARY KEY (id);


--
-- Name: rental_reservation rental_reservation_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_reservation
    ADD CONSTRAINT rental_reservation_pkey PRIMARY KEY (id);


--
-- Name: rental_testimonial rental_testimonial_guest_id_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial
    ADD CONSTRAINT rental_testimonial_guest_id_key UNIQUE (guest_id);


--
-- Name: rental_testimonial rental_testimonial_pkey; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial
    ADD CONSTRAINT rental_testimonial_pkey PRIMARY KEY (id);


--
-- Name: rental_testimonial rental_testimonial_reservation_id_key; Type: CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial
    ADD CONSTRAINT rental_testimonial_reservation_id_key UNIQUE (reservation_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_flatpage_sites_flatpage_id_078bbc8b; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_flatpage_sites_flatpage_id_078bbc8b ON public.django_flatpage_sites USING btree (flatpage_id);


--
-- Name: django_flatpage_sites_site_id_bfd8ea84; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_flatpage_sites_site_id_bfd8ea84 ON public.django_flatpage_sites USING btree (site_id);


--
-- Name: django_flatpage_url_41612362; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_flatpage_url_41612362 ON public.django_flatpage USING btree (url);


--
-- Name: django_flatpage_url_41612362_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_flatpage_url_41612362_like ON public.django_flatpage USING btree (url varchar_pattern_ops);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: rental_guest_email_ec445132_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_guest_email_ec445132_like ON public.rental_guest USING btree (email varchar_pattern_ops);


--
-- Name: rental_place_images_image_id_37c3bf7c; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_place_images_image_id_37c3bf7c ON public.rental_place_images USING btree (image_id);


--
-- Name: rental_place_images_place_id_853e3011; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_place_images_place_id_853e3011 ON public.rental_place_images USING btree (place_id);


--
-- Name: rental_place_name_88632e61_like; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_place_name_88632e61_like ON public.rental_place USING btree (name varchar_pattern_ops);


--
-- Name: rental_place_thumbnail_id_635534ca; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_place_thumbnail_id_635534ca ON public.rental_place USING btree (thumbnail_id);


--
-- Name: rental_reservation_guest_id_7ca3dbba; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_reservation_guest_id_7ca3dbba ON public.rental_reservation USING btree (guest_id);


--
-- Name: rental_reservation_place_id_cb42c6fb; Type: INDEX; Schema: public; Owner: nemausat
--

CREATE INDEX rental_reservation_place_id_cb42c6fb ON public.rental_reservation USING btree (place_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_flatpage_sites django_flatpage_site_flatpage_id_078bbc8b_fk_django_fl; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage_sites
    ADD CONSTRAINT django_flatpage_site_flatpage_id_078bbc8b_fk_django_fl FOREIGN KEY (flatpage_id) REFERENCES public.django_flatpage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_flatpage_sites django_flatpage_sites_site_id_bfd8ea84_fk_django_site_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_site_id_bfd8ea84_fk_django_site_id FOREIGN KEY (site_id) REFERENCES public.django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_place_images rental_place_images_image_id_37c3bf7c_fk_rental_image_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place_images
    ADD CONSTRAINT rental_place_images_image_id_37c3bf7c_fk_rental_image_id FOREIGN KEY (image_id) REFERENCES public.rental_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_place_images rental_place_images_place_id_853e3011_fk_rental_place_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place_images
    ADD CONSTRAINT rental_place_images_place_id_853e3011_fk_rental_place_id FOREIGN KEY (place_id) REFERENCES public.rental_place(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_place rental_place_thumbnail_id_635534ca_fk_rental_image_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_place
    ADD CONSTRAINT rental_place_thumbnail_id_635534ca_fk_rental_image_id FOREIGN KEY (thumbnail_id) REFERENCES public.rental_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_reservation rental_reservation_guest_id_7ca3dbba_fk_rental_guest_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_reservation
    ADD CONSTRAINT rental_reservation_guest_id_7ca3dbba_fk_rental_guest_id FOREIGN KEY (guest_id) REFERENCES public.rental_guest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_reservation rental_reservation_place_id_cb42c6fb_fk_rental_place_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_reservation
    ADD CONSTRAINT rental_reservation_place_id_cb42c6fb_fk_rental_place_id FOREIGN KEY (place_id) REFERENCES public.rental_place(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_testimonial rental_testimonial_guest_id_7b649bcd_fk_rental_guest_id; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial
    ADD CONSTRAINT rental_testimonial_guest_id_7b649bcd_fk_rental_guest_id FOREIGN KEY (guest_id) REFERENCES public.rental_guest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rental_testimonial rental_testimonial_reservation_id_2cf05dec_fk_rental_re; Type: FK CONSTRAINT; Schema: public; Owner: nemausat
--

ALTER TABLE ONLY public.rental_testimonial
    ADD CONSTRAINT rental_testimonial_reservation_id_2cf05dec_fk_rental_re FOREIGN KEY (reservation_id) REFERENCES public.rental_reservation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

