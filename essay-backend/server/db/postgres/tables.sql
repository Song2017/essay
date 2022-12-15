 create table "essay_article" (
    "essay_article_id" serial primary key,

    "title" varchar(100),
    "desc" varchar(100),
    "content" varchar,
    "img_url" varchar,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);

create table "essay_topic" (
    "essay_topic_id" serial primary key,

    "title" varchar(100),
    "img_url" varchar,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);

create table "essay_recommend" (
    "essay_recommend_id" serial primary key,

    "name" varchar(100),
    "img_url" varchar,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);

create table "app_user" (
    "app_user_id" serial primary key,

    "full_name" varchar(100),
    "email" varchar(100),
    "hashed_password" varchar,
    "is_active" boolean default true,
    "is_superuser" boolean default false,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);