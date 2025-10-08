-- Supabase schema for slackbot content pipeline

create table if not exists keywords (
    id serial primary key,
    keyword text not null,
    cleaned_keyword text,
    created_at timestamptz default now()
);

create table if not exists clusters (
    id serial primary key,
    name text not null,
    keywords int[],
    created_at timestamptz default now()
);

create table if not exists reports (
    id serial primary key,
    title text,
    filepath text,
    metadata jsonb,
    created_at timestamptz default now()
);
