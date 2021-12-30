-- CREATED BY ALDON

-- --------------------------------------------
-- Table Structure for SASARAN_LIFE_CYCLE_SPM
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.SASARAN_LIFE_CYCLE_SPM
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",


    -- Tulis Nama field yang diexcel di bawah ini:
	
	HAMIL int,
	USIA_0_sd_59_BULAN int,
	USIA_7_sd_15_TAHUN int,
	USIA_15_sd_59_TAHUN int,
	usia_lbh_dari_60_tahun int,



    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT SASARAN_LIFE_CYCLE_SPM_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.SASARAN_LIFE_CYCLE_SPM
    OWNER to postgres;

CREATE INDEX slcs_survei_individu_detail_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_survei_rumah_tangga_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX slcs_survei_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX slcs_provinsi_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_kecamatan_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_kelurahan_id_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_kd_puskesmas_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX slcs_HAMIL_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (HAMIL ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_USIA_0_sd_59_BULAN_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (USIA_0_sd_59_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_USIA_7_sd_15_TAHUN_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (USIA_7_sd_15_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_USIA_15_sd_59_TAHUN_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (USIA_15_sd_59_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX slcs_usia_lbh_dari_60_tahun_idx
    ON public.SASARAN_LIFE_CYCLE_SPM USING btree
    (usia_lbh_dari_60_tahun ASC NULLS LAST)
    TABLESPACE pg_default;



-- --------------------------------------------
-- Table Structure for KELUARGA_BERENCANA
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.KELUARGA_BERENCANA
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",


    -- Tulis Nama field yang diexcel di bawah ini:
	
	USIA_lebih_dari_10_TAHUN int,
	USIA_10_sd_54 int,
	WANITA_USIA_10_sd_54_KAWIN int,
	PRIA_USIA_lebih_dari_10_TAHUN_KAWIN int,
	WANITA_USIA_10_sd_54_DAN_PRIA_USIA_lebih_10_SUDAH_KAWIN int,
	WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL int,
	WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL_BER_KB int,
	wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb int,
	WANITA_BER_KB int,
	WANITA_TIDAK_BER_KB int,


    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT KELUARGA_BERENCANA_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.KELUARGA_BERENCANA
    OWNER to postgres;

CREATE INDEX kb_survei_individu_detail_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_survei_rumah_tangga_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kb_survei_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kb_provinsi_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_kecamatan_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_kelurahan_id_idx
    ON public.KELUARGA_BERENCANA USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_kd_puskesmas_idx
    ON public.KELUARGA_BERENCANA USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

	
CREATE INDEX kb_USIA_lebih_dari_10_TAHUN_idx
    ON public.KELUARGA_BERENCANA USING btree
    (USIA_lebih_dari_10_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_USIA_10_sd_54_idx
    ON public.KELUARGA_BERENCANA USING btree
    (USIA_10_sd_54 ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_USIA_10_sd_54_KAWIN_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_USIA_10_sd_54_KAWIN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_PRIA_USIA_lebih_dari_10_TAHUN_KAWIN_idx
    ON public.KELUARGA_BERENCANA USING btree
    (PRIA_USIA_lebih_dari_10_TAHUN_KAWIN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_USIA_10_sd_54_DAN_PRIA_USIA_lebih_10_SUDAH_KAWIN_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_USIA_10_sd_54_DAN_PRIA_USIA_lebih_10_SUDAH_KAWIN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL_BER_KB_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_USIA_10_sd_54_SUDAH_KAWIN_TIDAK_HAMIL_BER_KB ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb_idx
    ON public.KELUARGA_BERENCANA USING btree
    (wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_BER_KB_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_BER_KB ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kb_WANITA_TIDAK_BER_KB_idx
    ON public.KELUARGA_BERENCANA USING btree
    (WANITA_TIDAK_BER_KB ASC NULLS LAST)
    TABLESPACE pg_default;


-- --------------------------------------------
-- Table Structure for PERSALINAN_DI_FASKES
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.PERSALINAN_DI_FASKES
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",

    -- Tulis Nama field yang diexcel di bawah ini:
	
	IBU_DENGAN_ANAK_USIA_0_sd_11_BULAN	int,
	PERSALINAN_TIDAK_DI_FASKES	int,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT PERSALINAN_DI_FASKES_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.PERSALINAN_DI_FASKES
    OWNER to postgres;

CREATE INDEX persalinan_di_faskes_survei_individu_detail_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_survei_rumah_tangga_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX persalinan_di_faskes_survei_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX persalinan_di_faskes_provinsi_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_kecamatan_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_kelurahan_id_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_kd_puskesmas_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_IBU_DENGAN_ANAK_USIA_0_sd_11_BULAN_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (IBU_DENGAN_ANAK_USIA_0_sd_11_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX persalinan_di_faskes_PERSALINAN_TIDAK_DI_FASKES_idx
    ON public.PERSALINAN_DI_FASKES USING btree
    (PERSALINAN_TIDAK_DI_FASKES ASC NULLS LAST)
    TABLESPACE pg_default;

-- CREATED BY ALDON

-- CREATED BY DECA

-- --------------------------------------------
-- Table Structure for IMUNISASI_DASAR_LENGKAP
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.IMUNISASI_DASAR_LENGKAP
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
    MEMILIKI_BALITA_12_sd_23_BULAN int,
	SASARAN_TIDAK_IDL int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT IMUNISASI_DASAR_LENGKAP_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.IMUNISASI_DASAR_LENGKAP
    OWNER to postgres;


CREATE INDEX idi_survei_individu_detail_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX idi_survei_rumah_tangga_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX idi_survei_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX idi_provinsi_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX idi_kecamatan_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX idi_kelurahan_id_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX idi_kd_puskesmas_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX idi_MEMILIKI_BALITA_12_sd_23_BULAN_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (MEMILIKI_BALITA_12_sd_23_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX idi_SASARAN_TIDAK_IDL_idx
    ON public.IMUNISASI_DASAR_LENGKAP USING btree
    (SASARAN_TIDAK_IDL ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for ASI_EKSKLUSIF
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.ASI_EKSKLUSIF
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
    MEMILIKI_BAYI_7_sd_23_BULAN int,
	SASARAN_TIDAK_ASI_EKSLUSIF int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT ASI_EKSKLUSIF_pkey PRIMARY KEY (survei_individu_detail_id)
)
;

ALTER TABLE public.ASI_EKSKLUSIF
    OWNER to postgres;

CREATE INDEX asi_eksklusif_survei_individu_detail_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_survei_rumah_tangga_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_survei_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_provinsi_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_kecamatan_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_kelurahan_id_idx
    ON public.ASI_EKSKLUSIF USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_kd_puskesmas_idx
    ON public.ASI_EKSKLUSIF USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_MEMILIKI_BAYI_7_sd_23_BULAN_idx
    ON public.ASI_EKSKLUSIF USING btree
    (MEMILIKI_BAYI_7_sd_23_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX asi_eksklusif_SASARAN_TIDAK_ASI_EKSLUSIF_idx
    ON public.ASI_EKSKLUSIF USING btree
    (SASARAN_TIDAK_ASI_EKSLUSIF ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for TUMBUH_KEMBANG
-- --------------------------------------------


CREATE TABLE IF NOT EXISTS public.TUMBUH_KEMBANG
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	USIA_2_sd_59_BULAN int,
	SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT TUMBUH_KEMBANG_pkey PRIMARY KEY (survei_individu_detail_id)
)
;

ALTER TABLE public.TUMBUH_KEMBANG
    OWNER to postgres;

CREATE INDEX tumbuh_kembang_survei_individu_detail_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_survei_rumah_tangga_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_survei_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_provinsi_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_kecamatan_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_kelurahan_id_idx
    ON public.TUMBUH_KEMBANG USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_kd_puskesmas_idx
    ON public.TUMBUH_KEMBANG USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_USIA_2_sd_59_BULAN_idx
    ON public.TUMBUH_KEMBANG USING btree
    (USIA_2_sd_59_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tumbuh_kembang_SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN_idx
    ON public.TUMBUH_KEMBANG USING btree
    (SASARAN_TIDAK_PEMANTAUAN_PERTUMBUHAN ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for TB_PARU
-- --------------------------------------------


CREATE TABLE IF NOT EXISTS public.TB_PARU
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	lebih_dari_sama_dengan_15_TAHUN int,
	DIDIAGNOSIS_TB int,
	DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB int,
	PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR	int,
	SUSPEK_TB int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT TB_PARU_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.TB_PARU
    OWNER to postgres;

CREATE INDEX tb_paru_survei_individu_detail_id_idx
    ON public.TB_PARU USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_survei_rumah_tangga_id_idx
    ON public.TB_PARU USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_survei_id_idx
    ON public.TB_PARU USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_provinsi_id_idx
    ON public.TB_PARU USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_kecamatan_id_idx
    ON public.TB_PARU USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_kelurahan_id_idx
    ON public.TB_PARU USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_lebih_dari_sama_dengan_15_TAHUN_idx
    ON public.TB_PARU USING btree
    (lebih_dari_sama_dengan_15_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_DIDIAGNOSIS_TB_idx
    ON public.TB_PARU USING btree
    (DIDIAGNOSIS_TB ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB_idx
    ON public.TB_PARU USING btree
    (DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_TB ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR_idx
    ON public.TB_PARU USING btree
    (PENDERITA_TB_YANG_MINUM_OBAT_SESUAI_STANDAR ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX tb_paru_SUSPEK_TB_idx
    ON public.TB_PARU USING btree
    (SUSPEK_TB ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for ROKOK
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.ROKOK
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	INDIVIDU_MEROKOK int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT ROKOK_pkey PRIMARY KEY (survei_individu_detail_id)


)
;

ALTER TABLE public.ROKOK
    OWNER to postgres;

CREATE INDEX rokok_survei_individu_detail_id_idx
    ON public.ROKOK USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_survei_rumah_tangga_id_idx
    ON public.ROKOK USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_survei_id_idx
    ON public.ROKOK USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_provinsi_id_idx
    ON public.ROKOK USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_kecamatan_id_idx
    ON public.ROKOK USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_kelurahan_id_idx
    ON public.ROKOK USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_kd_puskesmas_idx
    ON public.ROKOK USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_INDIVIDU_MEROKOK_idx
    ON public.ROKOK USING btree
    (INDIVIDU_MEROKOK ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for JKN
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.JKN
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	BELUM_MENJADI_PESERTA_JKN int,
	PESERTA_JKN	int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT JKN_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.JKN
    OWNER to postgres;


CREATE INDEX jkn_survei_individu_detail_id_idx
    ON public.JKN USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_survei_rumah_tangga_id_idx
    ON public.JKN USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_survei_id_idx
    ON public.JKN USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_provinsi_id_idx
    ON public.JKN USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_kecamatan_id_idx
    ON public.JKN USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_kelurahan_id_idx
    ON public.JKN USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_kd_puskesmas_idx
    ON public.JKN USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_BELUM_MENJADI_PESERTA_JKN_idx
    ON public.JKN USING btree
    (BELUM_MENJADI_PESERTA_JKN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX jkn_PESERTA_JKN_idx
    ON public.JKN USING btree
    (PESERTA_JKN ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for PERILAKU_SAB
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.PERILAKU_SAB
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT PERILAKU_SAB_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.PERILAKU_SAB
    OWNER to postgres;

CREATE INDEX perilaku_sab_survei_individu_detail_id_idx
    ON public.PERILAKU_SAB USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_survei_rumah_tangga_id_idx
    ON public.PERILAKU_SAB USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_survei_id_idx
    ON public.PERILAKU_SAB USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_provinsi_id_idx
    ON public.PERILAKU_SAB USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_kecamatan_id_idx
    ON public.PERILAKU_SAB USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_kelurahan_id_idx
    ON public.PERILAKU_SAB USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_kd_puskesmas_idx
    ON public.PERILAKU_SAB USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_sab_IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU_idx
    ON public.PERILAKU_SAB USING btree
    (IND_SARANA_AIR_BERSIH_TERLINDUNG_PERILAKU ASC NULLS LAST)
    TABLESPACE pg_default;

-- --------------------------------------------
-- Table Structure for PERILAKU_JAMBAN
-- --------------------------------------------

CREATE TABLE IF NOT EXISTS public.PERILAKU_JAMBAN
(
    survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	IND_PUNYA_JAMBAN_SANITER_PERILAKU int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT PERILAKU_JAMBAN_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.PERILAKU_JAMBAN
    OWNER to postgres;

CREATE INDEX perilaku_jamban_survei_individu_detail_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_survei_rumah_tangga_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_survei_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_provinsi_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_kecamatan_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_kelurahan_id_idx
    ON public.PERILAKU_JAMBAN USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_kd_puskesmas_idx
    ON public.PERILAKU_JAMBAN USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX perilaku_jamban_IND_PUNYA_JAMBAN_SANITER_PERILAKU_idx
    ON public.PERILAKU_JAMBAN USING btree
    (IND_PUNYA_JAMBAN_SANITER_PERILAKU ASC NULLS LAST)
    TABLESPACE pg_default;

-- CREATED BY DECA

-- CREATED BY Aldi

CREATE TABLE IF NOT EXISTS public.KARAKTERISTIK_RESPONDEN
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",


    -- Tulis Nama field yang diexcel di bawah ini:
    UMUR_HARI_INI_TAHUN	int,
    UMUR_TAHUN	        int,
    UMURBULAN	        int,
    umur_bulan	            int,
    kategori_umur_bulan character varying(30) COLLATE pg_catalog."default",
    kategori_umur_tahun character varying(30) COLLATE pg_catalog."default",
    kategori_pendidikan character varying(30) COLLATE pg_catalog."default",
    kategori_pekerjaan character varying(30) COLLATE pg_catalog."default",
    Umur_5_sd_9_tahun	    int,
    Umur_10_sd_14_tahun	    int,
    Umur_15_24_tahun	    int,
    Umur_25_34_tahun	    int,
    Umur_35_44_tahun	    int,
    Umur_45_54_tahun	    int,
    Umur_55_64_tahun	    int,
    Umur_65_tahun_keatas	int,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT KARAKTERISTIK_RESPONDEN_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.KARAKTERISTIK_RESPONDEN
    OWNER to postgres;

CREATE INDEX kr_survei_individu_detail_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_survei_rumah_tangga_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kr_survei_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kr_provinsi_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_kecamatan_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_kelurahan_id_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_kd_puskesmas_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_UMUR_HARI_INI_TAHUN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (UMUR_HARI_INI_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_UMUR_TAHUN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (UMUR_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_UMURBULAN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (UMURBULAN ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kr_umur_bulan_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (umur_bulan ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_KATEGORI_UMUR_BULAN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (KATEGORI_UMUR_BULAN ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_KATEGORI_UMUR_TAHUN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (KATEGORI_UMUR_TAHUN ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_KATEGORI_PENDIDIKAN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (KATEGORI_PENDIDIKAN ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_KATEGORI_PEKERJAAN_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (KATEGORI_PEKERJAAN ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_5_sd_9_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_5_sd_9_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_10_sd_14_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_10_sd_14_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_15_24_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_15_24_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_25_34_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_25_34_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_35_44_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_35_44_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_45_54_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_45_54_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_55_64_tahun_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_55_64_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

    CREATE INDEX kr_Umur_65_tahun_keatas_idx
    ON public.KARAKTERISTIK_RESPONDEN USING btree
    (Umur_65_tahun_keatas ASC NULLS LAST)
    TABLESPACE pg_default;


-- CREATED BY Aldi


-- CREATED BY GERRY

CREATE TABLE IF NOT EXISTS public.Rokok_by_program
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	Perokok_umur_10_sd_18_tahun int,
	Perokok_umur_15_sd_18_tahun int,
	Perokok_umur_diatas_15_tahun int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT Rokok_by_program_pkey PRIMARY KEY (survei_individu_detail_id)

)
;


ALTER TABLE public.Rokok_by_program
    OWNER to postgres;

CREATE INDEX rokok_by_program_survei_individu_detail_id_idx
    ON public.Rokok_by_program USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX rokok_by_program_survei_rumah_tangga_id_idx
    ON public.Rokok_by_program USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX rokok_by_program_survei_id_idx
    ON public.Rokok_by_program USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX rokok_by_program_provinsi_id_idx
    ON public.Rokok_by_program USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_kecamatan_id_idx
    ON public.Rokok_by_program USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_kelurahan_id_idx
    ON public.Rokok_by_program USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_kd_puskesmas_idx
    ON public.Rokok_by_program USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_perokok_umur_10_sd_18_tahun_idx
    ON public.Rokok_by_program USING btree
    (perokok_umur_10_sd_18_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_perokok_umur_15_sd_18_tahun_idx
    ON public.Rokok_by_program USING btree
    (perokok_umur_15_sd_18_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokok_by_program_perokok_umur_diatas_15_tahun_idx
    ON public.Rokok_by_program USING btree
    (perokok_umur_diatas_15_tahun ASC NULLS LAST)
    TABLESPACE pg_default;
--------------------------------

CREATE TABLE IF NOT EXISTS public.Rokok_by_program_umur
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	Jumlah_umur_10_sd_18_tahun int,
	Jumlah_umur_15_sd_18_tahun int,
	Jumlah_umur_diatas_15_tahun int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT Rokok_by_program_umur_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.Rokok_by_program_umur
    OWNER to postgres;
   
CREATE INDEX Rokok_by_program_umur_survei_individu_detail_id_idx
    ON public.Rokok_by_program_umur USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX Rokok_by_program_umur_survei_rumah_tangga_id_idx
    ON public.Rokok_by_program_umur USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX Rokok_by_program_umur_survei_id_idx
    ON public.Rokok_by_program_umur USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX Rokok_by_program_umur_provinsi_id_idx
    ON public.Rokok_by_program_umur USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX Rokok_by_program_umur_kecamatan_id_idx
    ON public.Rokok_by_program_umur USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX Rokok_by_program_umur_kelurahan_id_idx
    ON public.Rokok_by_program_umur USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX Rokok_by_program_umur_kd_puskesmas_idx
    ON public.Rokok_by_program_umur USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX Rokok_by_program_umur_jumlah_umur_10_sd_18_tahun_idx
    ON public.Rokok_by_program_umur USING btree
    (jumlah_umur_10_sd_18_tahun ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX Rokok_by_program_umur_jumlah_umur_15_sd_18_tahun_idx
    ON public.Rokok_by_program_umur USING btree
    (jumlah_umur_15_sd_18_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX Rokok_by_program_umur_jumlah_umur_diatas_15_tahun_idx
    ON public.Rokok_by_program_umur USING btree
    (jumlah_umur_diatas_15_tahun ASC NULLS LAST)
    TABLESPACE pg_default;
 -----------------------------------------------------------------------------------
 
CREATE TABLE IF NOT EXISTS public.Denominator_KB
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14 int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49 int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54 int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT Denominator_KB_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.Denominator_KB
    OWNER to postgres;

CREATE INDEX denominator_KB_survei_individu_detail_id_idx
    ON public.Denominator_KB USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX denominator_kb_survei_rumah_tangga_id_idx
    ON public.Denominator_KB USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX denominator_kb_survei_id_idx
    ON public.Denominator_KB USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX denominator_kb_provinsi_id_idx
    ON public.Denominator_KB USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX denominator_kb_kecamatan_id_idx
    ON public.Denominator_KB USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX denominator_kb_kelurahan_id_idx
    ON public.Denominator_KB USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX denominator_kb_kd_puskesmas_idx
    ON public.Denominator_KB USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX denominator_kb_wanita_kawin_tidak_hamil_umur_10_sd_14_idx
    ON public.Denominator_KB USING btree
    (wanita_kawin_tidak_hamil_umur_10_sd_14 ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX denominator_kb_wanita_kawin_tidak_hamil_umur_15_sd_49_idx
    ON public.Denominator_KB USING btree
    (wanita_kawin_tidak_hamil_umur_15_sd_49 ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX denominator_kb_wanita_kawin_tidak_hamil_umur_50_sd_54_idx
    ON public.Denominator_KB USING btree
    (wanita_kawin_tidak_hamil_umur_50_sd_54 ASC NULLS LAST)
    TABLESPACE pg_default;        	
	
------------------------------------------------


CREATE TABLE IF NOT EXISTS public.KB_by_program
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_BER_sd_KB int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_BER_sd_KB int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_BER_sd_KB int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_10_sd_14_TIDAK_BER_sd_KB int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_15_sd_49_TIDAK_BER_sd_KB int,
	WANITA_KAWIN_TIDAK_HAMIL_UMUR_50_sd_54_TIDAK_BER_sd_KB int,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    CONSTRAINT KB_by_program_pkey PRIMARY KEY (survei_individu_detail_id)

)
;
    
ALTER TABLE public.KB_by_program
    OWNER to postgres;

-- kbp = KB_by_program

CREATE INDEX kbp_survei_individu_detail_id_idx
    ON public.KB_by_program USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kbp_survei_rumah_tangga_id_idx
    ON public.KB_by_program USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kbp_survei_id_idx
    ON public.KB_by_program USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX kbp_provinsi_id_idx
    ON public.KB_by_program USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_kecamatan_id_idx
    ON public.KB_by_program USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_kelurahan_id_idx
    ON public.KB_by_program USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_kd_puskesmas_idx
    ON public.KB_by_program USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
	
CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_10_sd_14_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_10_sd_14_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_15_sd_49_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_15_sd_49_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_50_sd_54_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_50_sd_54_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_10_sd_14_tidak_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_10_sd_14_tidak_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_15_sd_49_tidak_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_15_sd_49_tidak_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX kbp_wanita_kawin_tidak_hamil_umur_50_sd_54_tidak_ber_sd_kb_idx
    ON public.KB_by_program USING btree
    (wanita_kawin_tidak_hamil_umur_50_sd_54_tidak_ber_sd_kb ASC NULLS LAST)
    TABLESPACE pg_default;


-- CREATED BY GERRY

-- CREATED BY VIANTO

CREATE TABLE IF NOT EXISTS public.HIPERTENSI
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",


    -- Tulis Nama field yang diexcel di bawah ini:
    DIDIAGNOSIS_HIPERTENSI	int,
    INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI	int,
    INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR	int,
    DIUKUR_TEKANAN_DARAH	int,
    SISTOL	int,
    DIASTOL	int,
    SUSPEK_TEKANAN_DARAH_TINGGI	int,


    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT HIPERTENSI_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.HIPERTENSI
    OWNER to postgres;

CREATE INDEX hipertensi_survei_individu_detail_id_idx
    ON public.HIPERTENSI USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_survei_rumah_tangga_id_idx
    ON public.HIPERTENSI USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_survei_id_idx
    ON public.HIPERTENSI USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_provinsi_id_idx
    ON public.HIPERTENSI USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_kecamatan_id_idx
    ON public.HIPERTENSI USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_kelurahan_id_idx
    ON public.HIPERTENSI USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_kd_puskesmas_idx
    ON public.HIPERTENSI USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_DIDIAGNOSIS_HIPERTENSI_idx
    ON public.HIPERTENSI USING btree
    (DIDIAGNOSIS_HIPERTENSI ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_INDIVIDU_DIDIAGNOSIS_TAPI_TDK_MINUM_OBAT_HIPER_idx
    ON public.HIPERTENSI USING btree
    (INDIVIDU_DIDIAGNOSIS_TAPI_TIDAK_MINUM_OBAT_HIPERTENSI ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_INDIVIDU_DIDIAGNOSIS_HIPER_MINUM_OBAT_STANDAR_idx
    ON public.HIPERTENSI USING btree
    (INDIVIDU_DIDIAGNOSIS_HIPERTENSI_MINUM_OBAT_SESUAI_STANDAR ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_SISTOL_idx
    ON public.HIPERTENSI USING btree
    (SISTOL ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_DIASTOL_idx
    ON public.HIPERTENSI USING btree
    (DIASTOL ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX hipertensi_SUSPEK_TEKANAN_DARAH_TINGGI_idx
    ON public.HIPERTENSI USING btree
    (SUSPEK_TEKANAN_DARAH_TINGGI ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.ROKOKS
(
	survei_individu_detail_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_rumah_tangga_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	survei_id character varying(191) COLLATE pg_catalog."default" NOT NULL,
	provinsi_id character varying(2) COLLATE pg_catalog."default" NOT NULL,
    nama_provinsi character varying(191) COLLATE pg_catalog."default",
    kota_kabupaten_id character varying(4) COLLATE pg_catalog."default" NOT NULL,
    nama_kota_kabupaten character varying(191) COLLATE pg_catalog."default",
    kecamatan_id character varying(6) COLLATE pg_catalog."default" NOT NULL,
    nama_kecamatan character varying(191) COLLATE pg_catalog."default",
    kelurahan_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nama_kelurahan character varying(191) COLLATE pg_catalog."default",
    kd_puskesmas character varying(15) COLLATE pg_catalog."default" NOT NULL,
    nik character varying(16) COLLATE pg_catalog."default",
    nama character varying(191) COLLATE pg_catalog."default",
    tgl_lahir date,
    jenis_kelamin character varying(9) COLLATE pg_catalog."default",


    -- Tulis Nama field yang diexcel di bawah ini:
    Umur_5_9_tahun	int,
    Umur_10_14_tahun	int,
    Umur_15_24_tahun	int,
    Umur_25_34_tahun	int,
    Umur_35_44_tahun	int,
    Umur_45_54_tahun	int,
    Umur_55_64_tahun	int,
    Umur_65_tahun_keatas	int,


    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,

    CONSTRAINT ROKOKS_pkey PRIMARY KEY (survei_individu_detail_id)

)
;

ALTER TABLE public.ROKOKS
    OWNER to postgres;

CREATE INDEX rokoks_survei_individu_detail_id_idx
    ON public.ROKOKS USING btree
    (survei_individu_detail_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_survei_rumah_tangga_id_idx
    ON public.ROKOKS USING btree
    (survei_rumah_tangga_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_survei_id_idx
    ON public.ROKOKS USING btree
    (survei_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_provinsi_id_idx
    ON public.ROKOKS USING btree
    (provinsi_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_kecamatan_id_idx
    ON public.ROKOKS USING btree
    (kota_kabupaten_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_kelurahan_id_idx
    ON public.ROKOKS USING btree
    (kelurahan_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_kd_puskesmas_idx
    ON public.ROKOKS USING btree
    (kd_puskesmas COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


-- buat
CREATE INDEX rokoks_Umur_5_9_tahun_rokoks_idx
    ON public.ROKOKS USING btree
    (Umur_5_9_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_10_14_tahun_rokoks_idx
    ON public.ROKOKS USING btree
    (Umur_10_14_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_15_24_tahun_idx
    ON public.ROKOKS USING btree
    (Umur_15_24_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_25_34_tahun_idx
    ON public.ROKOKS USING btree
    (Umur_25_34_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_35_44_tahun_idx
    ON public.ROKOKS USING btree
    (Umur_35_44_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_45_54_tahun_idx
    ON public.ROKOKS USING btree
    (Umur_45_54_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_55_64_tahun_idx
    ON public.ROKOKS USING btree
    (Umur_55_64_tahun ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX rokoks_Umur_65_tahun_keatas_idx
    ON public.ROKOKS USING btree
    (Umur_65_tahun_keatas ASC NULLS LAST)
    TABLESPACE pg_default;


-- CREATED BY VIANTO