-- Table: public.raw_survei

-- DROP TABLE public.raw_survei;

CREATE TABLE IF NOT EXISTS public.raw_survei
(
    survei_survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_tanggal date,
    survei_no_urut_rt character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_no_urut_kel character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_surveyor character varying(191) COLLATE pg_catalog."default",
    survei_supervisor character varying(191) COLLATE pg_catalog."default",
    survei_no_kk character(191) COLLATE pg_catalog."default",
    survei_nama_kk character varying(191) COLLATE pg_catalog."default",
    survei_alamat text COLLATE pg_catalog."default" NOT NULL,
    survei_propinsi_id character(2) COLLATE pg_catalog."default" NOT NULL,
    survei_kota_id character(4) COLLATE pg_catalog."default" NOT NULL,
    survei_kecamatan_id character(6) COLLATE pg_catalog."default" NOT NULL,
    survei_kelurahan_id character(10) COLLATE pg_catalog."default" NOT NULL,
    survei_kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    survei_nm_kota character varying(191) COLLATE pg_catalog."default",
    survei_nm_propinsi character varying(191) COLLATE pg_catalog."default",
    survei_nm_kecamatan character varying(191) COLLATE pg_catalog."default",
    survei_nm_kelurahan character varying(191) COLLATE pg_catalog."default",
    survei_iks_besar double precision,
    survei_iks_inti double precision,
    survei_rt_new character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_rw_new character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_kode character varying(191) COLLATE pg_catalog."default",
    survei_created_at timestamp without time zone,
    survei_updated_at timestamp without time zone,
    survei_status_pindah smallint DEFAULT 0,
    survei_status_delete smallint NOT NULL,
    survei_step_number smallint NOT NULL,
    survei_sumber character varying(255) COLLATE pg_catalog."default",
    survei_status_kepala_keluarga smallint NOT NULL DEFAULT 0,
    survei_rt_old character varying(191) COLLATE pg_catalog."default",
    survei_rw_old character varying(191) COLLATE pg_catalog."default",
    survei_status_migrasi integer,
    survei_catatan_migrasi text COLLATE pg_catalog."default",
    survei_iks_inti_old double precision,
    survei_iks_besar_old double precision,
    survei_deleted_at timestamp without time zone,
    survei_survei_id_old integer,
    survei_rt_survei_rt_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_rt_jml_art integer,
    survei_rt_jml_art_wawancara integer,
    survei_rt_jml_art_dewasa integer,
    survei_rt_jml_art_10_54_thn integer,
    survei_rt_jml_art_12_59_bln integer,
    survei_rt_jml_art_0_11_bln integer,
    survei_rt_sab character(1) COLLATE pg_catalog."default",
    survei_rt_sat character(1) COLLATE pg_catalog."default",
    survei_rt_jk character(1) COLLATE pg_catalog."default",
    survei_rt_js character(1) COLLATE pg_catalog."default",
    survei_rt_gjb character(1) COLLATE pg_catalog."default",
    survei_rt_obat_gjb character(1) COLLATE pg_catalog."default",
    survei_rt_pasung character(1) COLLATE pg_catalog."default",
    survei_rt_keterangan text COLLATE pg_catalog."default",
    survei_rt_kode character varying(75) COLLATE pg_catalog."default",
    survei_rt_supervisor integer,
    survei_rt_surveyor integer,
    survei_rt_indikator_8 character(1) COLLATE pg_catalog."default",
    survei_rt_indikator_11 character(1) COLLATE pg_catalog."default",
    survei_rt_indikator_12 character(1) COLLATE pg_catalog."default",
    survei_rt_status_delete smallint NOT NULL DEFAULT 0,
    survei_rt_created_at timestamp without time zone,
    survei_rt_updated_at timestamp without time zone,
    survei_rt_deleted_at timestamp without time zone,
    survei_rt_status_migrasi integer,
    survei_rt_catatan_migrasi text COLLATE pg_catalog."default",
    survei_rt_kd_puskesmas character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_rt_survei_id_old integer,
    survei_individu_survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_individu_jkn character(1) COLLATE pg_catalog."default",
    survei_individu_merokok character(1) COLLATE pg_catalog."default",
    survei_individu_babj character(1) COLLATE pg_catalog."default",
    survei_individu_sab character(1) COLLATE pg_catalog."default",
    survei_individu_tb character(1) COLLATE pg_catalog."default",
    survei_individu_obat_tb character(1) COLLATE pg_catalog."default",
    survei_individu_batuk character(1) COLLATE pg_catalog."default",
    survei_individu_hipertensi character(1) COLLATE pg_catalog."default",
    survei_individu_obat_hipertensi character(1) COLLATE pg_catalog."default",
    survei_individu_tekanan_darah character(1) COLLATE pg_catalog."default",
    survei_individu_sistolik double precision,
    survei_individu_diastolik double precision,
    survei_individu_kb character(1) COLLATE pg_catalog."default",
    survei_individu_kb_follow character varying(191) COLLATE pg_catalog."default",
    survei_individu_kb_detail smallint,
    survei_individu_faskes character(1) COLLATE pg_catalog."default",
    survei_individu_asi_ekslusif character(1) COLLATE pg_catalog."default",
    survei_individu_imunisasi character(1) COLLATE pg_catalog."default",
    survei_individu_pantau_balita character(1) COLLATE pg_catalog."default",
    survei_individu_keterangan text COLLATE pg_catalog."default",
    survei_individu_catatan_intervensi text COLLATE pg_catalog."default",
    survei_individu_no_urut_rt character varying(191) COLLATE pg_catalog."default",
    survei_individu_no_urut_kel character varying(191) COLLATE pg_catalog."default",
    survei_individu_nik character(16) COLLATE pg_catalog."default",
    survei_individu_status_nik integer,
    survei_individu_nama character varying(75) COLLATE pg_catalog."default",
    survei_individu_hub_kel_id smallint,
    survei_individu_tanggal_lahir date,
    survei_individu_umur_bln smallint,
    survei_individu_umur_thn smallint,
    survei_individu_jk_id smallint,
    survei_individu_stmarital_id smallint,
    survei_individu_wuh character(1) COLLATE pg_catalog."default",
    survei_individu_agama_id smallint,
    survei_individu_pendidikan_id smallint,
    survei_individu_pekerjaan_id smallint,
    survei_individu_indikator_1 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_2 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_3 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_4 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_5 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_6 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_7 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_8 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_9 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_10 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_11 character(1) COLLATE pg_catalog."default",
    survei_individu_indikator_12 character(1) COLLATE pg_catalog."default",
    survei_individu_kode character varying(75) COLLATE pg_catalog."default",
    survei_individu_supervisor integer,
    survei_individu_surveyor integer,
    survei_individu_status_delete smallint NOT NULL DEFAULT 0,
    survei_individu_created_at timestamp without time zone,
    survei_individu_updated_at timestamp without time zone,
    survei_individu_survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_individu_status_survei smallint,
    survei_individu_deleted_at timestamp without time zone,
    survei_individu_status_migrasi integer,
    survei_individu_catatan_migrasi text COLLATE pg_catalog."default",
    survei_individu_kd_puskesmas character varying(191) COLLATE pg_catalog."default" NOT NULL,
    survei_individu_survei_id_old integer,
    CONSTRAINT pk_raw_survei1 PRIMARY KEY (survei_individu_survei_individu_detail_id)
)

TABLESPACE pg_default;

ALTER TABLE public.raw_survei
    OWNER to postgres;

COMMENT ON COLUMN public.raw_survei.survei_sumber
    IS 'web or mobile';

COMMENT ON COLUMN public.raw_survei.survei_status_kepala_keluarga
    IS 'kepala keluarga ada atau tidak';

COMMENT ON COLUMN public.raw_survei.survei_individu_kb_follow
    IS 'uuid v5';

COMMENT ON COLUMN public.raw_survei.survei_individu_survei_id
    IS 'uuid v5';
-- Index: survei_individu_survei_id1

-- DROP INDEX public.survei_individu_survei_id1;

CREATE INDEX survei_individu_survei_id1
    ON public.raw_survei USING btree
    (survei_individu_survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_kd_puskesmas1

-- DROP INDEX public.survei_kd_puskesmas1;

CREATE INDEX survei_kd_puskesmas1
    ON public.raw_survei USING btree
    (survei_kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_kecamatan_id1

-- DROP INDEX public.survei_kecamatan_id1;

CREATE INDEX survei_kecamatan_id1
    ON public.raw_survei USING btree
    (survei_kecamatan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_kelurahan_id1

-- DROP INDEX public.survei_kelurahan_id1;

CREATE INDEX survei_kelurahan_id1
    ON public.raw_survei USING btree
    (survei_kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_kota_id1

-- DROP INDEX public.survei_kota_id1;

CREATE INDEX survei_kota_id1
    ON public.raw_survei USING btree
    (survei_kota_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_propinsi_id1

-- DROP INDEX public.survei_propinsi_id1;

CREATE INDEX survei_propinsi_id1
    ON public.raw_survei USING btree
    (survei_propinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_survei_id1

-- DROP INDEX public.survei_survei_id1;

CREATE INDEX survei_survei_id1
    ON public.raw_survei USING btree
    (survei_survei_id COLLATE pg_catalog."default" ASC NULLS LAST, survei_rt_survei_rt_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: survei_tanggal1

-- DROP INDEX public.survei_tanggal1;

CREATE INDEX survei_tanggal1
    ON public.raw_survei USING btree
    (survei_tanggal ASC NULLS LAST)
    TABLESPACE pg_default;
