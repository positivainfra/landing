-- Tabla de lista de espera de la landing pública (positiva.studio).
-- ⚠️ Va en una instancia de Supabase NUEVA y SEPARADA, exclusiva de la web pública.
--    NO ejecutar contra la base de datos de la app (test./producción).

create table if not exists public.waitlist (
  id         bigint generated always as identity primary key,
  email      text        not null unique,
  source     text        not null default 'landing',
  created_at timestamptz not null default now()
);

-- RLS activado y sin políticas públicas: solo la service_role key (que las omite),
-- usada por la Pages Function del servidor, puede leer/escribir. El cliente anon no.
alter table public.waitlist enable row level security;
