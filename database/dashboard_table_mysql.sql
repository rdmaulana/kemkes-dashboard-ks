-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2021 at 04:06 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dashboardtable`
--

-- --------------------------------------------------------

--
-- Table structure for table `asi_eksklusif`
--

CREATE TABLE `asi_eksklusif` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id_8` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik_13` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `memiliki_bayi_7_sd_23_bulan` int(11) DEFAULT NULL,
  `sasaran_tidak_asi_ekslusif` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at_20` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `denominator_kb`
--

CREATE TABLE `denominator_kb` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id_8` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan_11` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas_12` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir_15` date DEFAULT NULL,
  `jenis_kelamin_16` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_10_sd_14_17` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_15_sd_49` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_50_sd_54_19` int(11) DEFAULT NULL,
  `created_at_20` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hipertensi`
--

CREATE TABLE `hipertensi` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id_4` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id_6` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas_12` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir_15` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `didiagnosis_hipertensi_17` int(11) DEFAULT NULL,
  `individu_didiagnosis_tapi_tidak_minum_obat_hipertensi_18` int(11) DEFAULT NULL,
  `individu_didiagnosis_hipertensi_minum_obat_sesuai_standar` int(11) DEFAULT NULL,
  `diukur_tekanan_darah` int(11) DEFAULT NULL,
  `sistol` int(11) DEFAULT NULL,
  `diastol` int(11) DEFAULT NULL,
  `suspek_tekanan_darah_tinggi` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `imunisasi_dasar_lengkap`
--

CREATE TABLE `imunisasi_dasar_lengkap` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id_2` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin_16` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `memiliki_balita_12_sd_23_bulan` int(11) DEFAULT NULL,
  `sasaran_tidak_idl` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `jkn`
--

CREATE TABLE `jkn` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan_11` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama_14` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir_15` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `belum_menjadi_peserta_jkn` int(11) DEFAULT NULL,
  `peserta_jkn_18` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at_20` timestamp NULL DEFAULT NULL,
  `deleted_at_21` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `karakteristik_responden`
--

CREATE TABLE `karakteristik_responden` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id_4` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir_15` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `umur_hari_ini_tahun_17` int(11) DEFAULT NULL,
  `umur_tahun` int(11) DEFAULT NULL,
  `umurbulan` int(11) DEFAULT NULL,
  `umur_bulan_20` int(11) DEFAULT NULL,
  `kategori_umur_bulan_21` int(11) DEFAULT NULL,
  `kategori_umur_tahun` int(11) DEFAULT NULL,
  `kategori_pendidikan_23` int(11) DEFAULT NULL,
  `kategori_pekerjaan` int(11) DEFAULT NULL,
  `umur_5_sd_9_tahun` int(11) DEFAULT NULL,
  `umur_10_sd_14_tahun` int(11) DEFAULT NULL,
  `umur_15_24_tahun` int(11) DEFAULT NULL,
  `umur_25_34_tahun` int(11) DEFAULT NULL,
  `umur_35_44_tahun` int(11) DEFAULT NULL,
  `umur_45_54_tahun` int(11) DEFAULT NULL,
  `umur_55_64_tahun` int(11) DEFAULT NULL,
  `umur_65_tahun_keatas_32` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `kb_by_program`
--

CREATE TABLE `kb_by_program` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_10_sd_14_ber_sd_kb_17` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_15_sd_49_ber_sd_kb_18` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_50_sd_54_ber_sd_kb` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_10_sd_14_tidak_ber_sd_kb` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_15_sd_49_tidak_ber_sd_kb` int(11) DEFAULT NULL,
  `wanita_kawin_tidak_hamil_umur_50_sd_54_tidak_ber_sd_kb` int(11) DEFAULT NULL,
  `created_at_23` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `keluarga_berencana`
--

CREATE TABLE `keluarga_berencana` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id_3` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id_4` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas_12` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik_13` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama_14` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `usia_lebih_dari_10_tahun_17` int(11) DEFAULT NULL,
  `usia_10_sd_54` int(11) DEFAULT NULL,
  `wanita_usia_10_sd_54_kawin` int(11) DEFAULT NULL,
  `pria_usia_lebih_dari_10_tahun_kawin_20` int(11) DEFAULT NULL,
  `wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin` int(11) DEFAULT NULL,
  `wanita_usia_10_sd_54_sudah_kawin_tidak_hamil` int(11) DEFAULT NULL,
  `wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb` int(11) DEFAULT NULL,
  `wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb_24` int(11) DEFAULT NULL,
  `wanita_ber_kb` int(11) DEFAULT NULL,
  `wanita_tidak_ber_kb` int(11) DEFAULT NULL,
  `created_at_27` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `perilaku_jamban`
--

CREATE TABLE `perilaku_jamban` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id_2` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id_3` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `ind_punya_jamban_saniter_perilaku` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `perilaku_sab`
--

CREATE TABLE `perilaku_sab` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `ind_sarana_air_bersih_terlindung_perilaku` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at_19` timestamp NULL DEFAULT NULL,
  `deleted_at_20` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `persalinan_di_faskes`
--

CREATE TABLE `persalinan_di_faskes` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id_2` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik_13` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `ibu_dengan_anak_usia_0_sd_11_bulan` int(11) DEFAULT NULL,
  `persalinan_tidak_di_faskes_18` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at_20` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rokok`
--

CREATE TABLE `rokok` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id_8` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id_10` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `individu_merokok` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rokoks`
--

CREATE TABLE `rokoks` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id_10` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas_12` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama_14` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `umur_5_9_tahun` int(11) DEFAULT NULL,
  `umur_10_14_tahun` int(11) DEFAULT NULL,
  `umur_15_24_tahun_19` int(11) DEFAULT NULL,
  `umur_25_34_tahun_20` int(11) DEFAULT NULL,
  `umur_35_44_tahun` int(11) DEFAULT NULL,
  `umur_45_54_tahun` int(11) DEFAULT NULL,
  `umur_55_64_tahun` int(11) DEFAULT NULL,
  `umur_65_tahun_keatas_24` int(11) DEFAULT NULL,
  `created_at_26` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rokok_by_program`
--

CREATE TABLE `rokok_by_program` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id_4` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id_6` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan_9` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan_11` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `perokok_umur_10_sd_18_tahun` int(11) DEFAULT NULL,
  `perokok_umur_15_sd_18_tahun_18` int(11) DEFAULT NULL,
  `perokok_umur_diatas_15_tahun_19` int(11) DEFAULT NULL,
  `created_at_20` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at_22` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rokok_by_program_umur`
--

CREATE TABLE `rokok_by_program_umur` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id_6` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan_11` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik_13` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `jumlah_umur_10_sd_18_tahun` int(11) DEFAULT NULL,
  `jumlah_umur_15_sd_18_tahun` int(11) DEFAULT NULL,
  `jumlah_umur_diatas_15_tahun_19` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sasaran_life_cycle_spm`
--

CREATE TABLE `sasaran_life_cycle_spm` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id_2` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id_4` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten_7` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id_8` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id_10` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin_16` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `hamil` int(11) DEFAULT NULL,
  `usia_0_sd_59_bulan_18` int(11) DEFAULT NULL,
  `usia_7_sd_15_tahun` int(11) DEFAULT NULL,
  `usia_15_sd_59_tahun` int(11) DEFAULT NULL,
  `usia_≥_60_tahun` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_paru`
--

CREATE TABLE `tb_paru` (
  `survei_individu_detail_id_1` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas_12` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir_15` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `≥15_tahun` int(11) DEFAULT NULL,
  `didiagnosis_tb` int(11) DEFAULT NULL,
  `didiagnosis_tapi_tidak_minum_obat_tb` int(11) DEFAULT NULL,
  `penderita_tb_yang_minum_obat_sesuai_standar` int(11) DEFAULT NULL,
  `suspek_tb` int(11) DEFAULT NULL,
  `created_at_22` timestamp NULL DEFAULT NULL,
  `updated_at_23` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tumbuh_kembang`
--

CREATE TABLE `tumbuh_kembang` (
  `survei_individu_detail_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_rumah_tangga_id_2` varchar(191) CHARACTER SET utf8 NOT NULL,
  `survei_id` varchar(191) CHARACTER SET utf8 NOT NULL,
  `provinsi_id` varchar(2) CHARACTER SET utf8 NOT NULL,
  `nama_provinsi_5` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kota_kabupaten_id` varchar(4) CHARACTER SET utf8 NOT NULL,
  `nama_kota_kabupaten` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kecamatan_id_8` varchar(6) CHARACTER SET utf8 NOT NULL,
  `nama_kecamatan` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kelurahan_id` varchar(10) CHARACTER SET utf8 NOT NULL,
  `nama_kelurahan_11` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `kd_puskesmas` varchar(15) CHARACTER SET utf8 NOT NULL,
  `nik` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `nama` varchar(191) CHARACTER SET utf8 DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `jenis_kelamin` varchar(9) CHARACTER SET utf8 DEFAULT NULL,
  `usia_2_sd_59_bulan` int(11) DEFAULT NULL,
  `sasaran_tidak_pemantauan_pertumbuhan` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asi_eksklusif`
--
ALTER TABLE `asi_eksklusif`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `asi_eksklusif_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `asi_eksklusif_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `asi_eksklusif_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `asi_eksklusif_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `asi_eksklusif_survei_id_idx` (`survei_id`),
  ADD KEY `asi_eksklusif_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `asi_eksklusif_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`),
  ADD KEY `asi_eksklusif_sasaran_tidak_asi_ekslusif_idx` (`sasaran_tidak_asi_ekslusif`),
  ADD KEY `asi_eksklusif_memiliki_bayi_7_sd_23_bulan_idx` (`memiliki_bayi_7_sd_23_bulan`);

--
-- Indexes for table `denominator_kb`
--
ALTER TABLE `denominator_kb`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `denominator_kb_survei_id_idx` (`survei_id`),
  ADD KEY `denominator_kb_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `denominator_kb_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `denominator_kb_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `denominator_kb_wanita_kawin_tidak_hamil_umur_50_sd_54_idx` (`wanita_kawin_tidak_hamil_umur_50_sd_54_19`),
  ADD KEY `denominator_kb_kd_puskesmas_idx` (`kd_puskesmas_12`),
  ADD KEY `denominator_kb_wanita_kawin_tidak_hamil_umur_15_sd_49_idx` (`wanita_kawin_tidak_hamil_umur_15_sd_49`),
  ADD KEY `denominator_kb_wanita_kawin_tidak_hamil_umur_10_sd_14_idx` (`wanita_kawin_tidak_hamil_umur_10_sd_14_17`),
  ADD KEY `denominator_kb_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `denominator_kb_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id_2`);

--
-- Indexes for table `hipertensi`
--
ALTER TABLE `hipertensi`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `hipertensi_kecamatan_id_idx` (`kota_kabupaten_id_6`),
  ADD KEY `hipertensi_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `hipertensi_diastol_idx` (`diastol`),
  ADD KEY `hipertensi_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `hipertensi_suspek_tekanan_darah_tinggi_idx` (`suspek_tekanan_darah_tinggi`),
  ADD KEY `hipertensi_sistol_idx` (`sistol`),
  ADD KEY `hipertensi_individu_didiagnosis_hiper_minum_obat_standar_idx` (`individu_didiagnosis_hipertensi_minum_obat_sesuai_standar`),
  ADD KEY `hipertensi_individu_didiagnosis_tapi_tdk_minum_obat_hiper_idx` (`individu_didiagnosis_tapi_tidak_minum_obat_hipertensi_18`),
  ADD KEY `hipertensi_didiagnosis_hipertensi_idx` (`didiagnosis_hipertensi_17`),
  ADD KEY `hipertensi_kd_puskesmas_idx` (`kd_puskesmas_12`),
  ADD KEY `hipertensi_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `hipertensi_survei_id_idx` (`survei_id`),
  ADD KEY `hipertensi_provinsi_id_idx` (`provinsi_id_4`);

--
-- Indexes for table `imunisasi_dasar_lengkap`
--
ALTER TABLE `imunisasi_dasar_lengkap`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `idi_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `idi_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id_2`),
  ADD KEY `idi_memiliki_balita_12_sd_23_bulan_idx` (`memiliki_balita_12_sd_23_bulan`),
  ADD KEY `idi_sasaran_tidak_idl_idx` (`sasaran_tidak_idl`),
  ADD KEY `idi_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `idi_survei_id_idx` (`survei_id`),
  ADD KEY `idi_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `idi_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `idi_kd_puskesmas_idx` (`kd_puskesmas`);

--
-- Indexes for table `jkn`
--
ALTER TABLE `jkn`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `jkn_peserta_jkn_idx` (`peserta_jkn_18`),
  ADD KEY `jkn_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `jkn_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `jkn_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `jkn_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `jkn_survei_id_idx` (`survei_id`),
  ADD KEY `jkn_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `jkn_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `jkn_belum_menjadi_peserta_jkn_idx` (`belum_menjadi_peserta_jkn`);

--
-- Indexes for table `karakteristik_responden`
--
ALTER TABLE `karakteristik_responden`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `kr_kategori_pendidikan_idx` (`kategori_pendidikan_23`),
  ADD KEY `kr_umurbulan_idx` (`umurbulan`),
  ADD KEY `kr_umur_bulan_idx` (`umur_bulan_20`),
  ADD KEY `kr_kategori_umur_bulan_idx` (`kategori_umur_bulan_21`),
  ADD KEY `kr_kategori_umur_tahun_idx` (`kategori_umur_tahun`),
  ADD KEY `kr_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `kr_kategori_pekerjaan_idx` (`kategori_pekerjaan`),
  ADD KEY `kr_umur_5_sd_9_tahun_idx` (`umur_5_sd_9_tahun`),
  ADD KEY `kr_umur_10_sd_14_tahun_idx` (`umur_10_sd_14_tahun`),
  ADD KEY `kr_umur_15_24_tahun_idx` (`umur_15_24_tahun`),
  ADD KEY `kr_umur_25_34_tahun_idx` (`umur_25_34_tahun`),
  ADD KEY `kr_umur_35_44_tahun_idx` (`umur_35_44_tahun`),
  ADD KEY `kr_umur_45_54_tahun_idx` (`umur_45_54_tahun`),
  ADD KEY `kr_umur_55_64_tahun_idx` (`umur_55_64_tahun`),
  ADD KEY `kr_umur_65_tahun_keatas_idx` (`umur_65_tahun_keatas_32`),
  ADD KEY `kr_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `kr_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `kr_provinsi_id_idx` (`provinsi_id_4`),
  ADD KEY `kr_survei_id_idx` (`survei_id`),
  ADD KEY `kr_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `kr_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`),
  ADD KEY `kr_umur_tahun_idx` (`umur_tahun`),
  ADD KEY `kr_umur_hari_ini_tahun_idx` (`umur_hari_ini_tahun_17`);

--
-- Indexes for table `kb_by_program`
--
ALTER TABLE `kb_by_program`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_10_sd_14_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_10_sd_14_ber_sd_kb_17`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_50_sd_54_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_50_sd_54_ber_sd_kb`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_10_sd_14_tidak_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_10_sd_14_tidak_ber_sd_kb`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_15_sd_49_tidak_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_15_sd_49_tidak_ber_sd_kb`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_50_sd_54_tidak_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_50_sd_54_tidak_ber_sd_kb`),
  ADD KEY `kbp_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`),
  ADD KEY `kbp_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `kbp_survei_id_idx` (`survei_id`),
  ADD KEY `kbp_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `kbp_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `kbp_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `kbp_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `kbp_wanita_kawin_tidak_hamil_umur_15_sd_49_ber_sd_kb_idx` (`wanita_kawin_tidak_hamil_umur_15_sd_49_ber_sd_kb_18`);

--
-- Indexes for table `keluarga_berencana`
--
ALTER TABLE `keluarga_berencana`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `idi_pria_usia_lebih_dari_10_tahun_kawin_idx` (`pria_usia_lebih_dari_10_tahun_kawin_20`),
  ADD KEY `idi_wanita_usia_10_sd_54_kawin_idx` (`wanita_usia_10_sd_54_kawin`),
  ADD KEY `idi_wanita_tidak_ber_kb_idx` (`wanita_tidak_ber_kb`),
  ADD KEY `idi_wanita_ber_kb_idx` (`wanita_ber_kb`),
  ADD KEY `idi_wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb_idx` (`wanita_usia_10_sd_54_sudahkawin_tidak_hamil_tidak_berkb_24`),
  ADD KEY `idi_wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb_idx` (`wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_ber_kb`),
  ADD KEY `idi_usia_10_sd_54_idx` (`usia_10_sd_54`),
  ADD KEY `idi_usia_lebih_dari_10_tahun_idx` (`usia_lebih_dari_10_tahun_17`),
  ADD KEY `idi_wanita_usia_10_sd_54_sudah_kawin_tidak_hamil_idx` (`wanita_usia_10_sd_54_sudah_kawin_tidak_hamil`),
  ADD KEY `idi_wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin_idx` (`wanita_usia_10_sd_54_dan_pria_usia_lebih_10_sudah_kawin`);

--
-- Indexes for table `perilaku_jamban`
--
ALTER TABLE `perilaku_jamban`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `perilaku_jamban_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `perilaku_jamban_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`),
  ADD KEY `perilaku_jamban_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id_2`),
  ADD KEY `perilaku_jamban_survei_id_idx` (`survei_id_3`),
  ADD KEY `perilaku_jamban_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `perilaku_jamban_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `perilaku_jamban_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `perilaku_jamban_ind_punya_jamban_saniter_perilaku_idx` (`ind_punya_jamban_saniter_perilaku`);

--
-- Indexes for table `perilaku_sab`
--
ALTER TABLE `perilaku_sab`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `perilaku_sab_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `perilaku_sab_survei_id_idx` (`survei_id`),
  ADD KEY `perilaku_sab_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `perilaku_sab_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `perilaku_sab_ind_sarana_air_bersih_terlindung_perilaku_idx` (`ind_sarana_air_bersih_terlindung_perilaku`),
  ADD KEY `perilaku_sab_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `perilaku_sab_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `perilaku_sab_kecamatan_id_idx` (`kota_kabupaten_id`);

--
-- Indexes for table `persalinan_di_faskes`
--
ALTER TABLE `persalinan_di_faskes`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `idi_ibu_dengan_anak_usia_0_sd_11_bulan_idx` (`ibu_dengan_anak_usia_0_sd_11_bulan`),
  ADD KEY `idi_persalinan_tidak_di_faskes_idx` (`persalinan_tidak_di_faskes_18`);

--
-- Indexes for table `rokok`
--
ALTER TABLE `rokok`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `rokok_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `rokok_kelurahan_id_idx` (`kelurahan_id_10`),
  ADD KEY `rokok_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `rokok_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `rokok_individu_merokok_idx` (`individu_merokok`),
  ADD KEY `rokok_survei_id_idx` (`survei_id`),
  ADD KEY `rokok_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `rokok_kd_puskesmas_idx` (`kd_puskesmas`);

--
-- Indexes for table `rokoks`
--
ALTER TABLE `rokoks`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `rokoks_no_idx` (`no`),
  ADD KEY `rokoks_umur_45_54_tahun_idx` (`umur_45_54_tahun`),
  ADD KEY `rokoks_umur_35_44_tahun_idx` (`umur_35_44_tahun`),
  ADD KEY `rokoks_umur_25_34_tahun_idx` (`umur_25_34_tahun_20`),
  ADD KEY `rokoks_umur_15_24_tahun_idx` (`umur_15_24_tahun_19`),
  ADD KEY `rokoks_umur_10_14_tahun_rokoks_idx` (`umur_10_14_tahun`),
  ADD KEY `rokoks_umur_5_9_tahun_rokoks_idx` (`umur_5_9_tahun`),
  ADD KEY `rokoks_kd_puskesmas_idx` (`kd_puskesmas_12`),
  ADD KEY `rokoks_kelurahan_id_idx` (`kelurahan_id_10`),
  ADD KEY `rokoks_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `rokoks_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `rokoks_survei_id_idx` (`survei_id`),
  ADD KEY `rokoks_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `rokoks_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `rokoks_umur_55_64_tahun_idx` (`umur_55_64_tahun`),
  ADD KEY `rokoks_umur_65_tahun_keatas_idx` (`umur_65_tahun_keatas_24`);

--
-- Indexes for table `rokok_by_program`
--
ALTER TABLE `rokok_by_program`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `rokok_by_program_perokok_umur_15_sd_18_tahun_idx` (`perokok_umur_15_sd_18_tahun_18`),
  ADD KEY `rokok_by_program_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `rokok_by_program_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `rokok_by_program_provinsi_id_idx` (`provinsi_id_4`),
  ADD KEY `rokok_by_program_survei_id_idx` (`survei_id`),
  ADD KEY `rokok_by_program_kecamatan_id_idx` (`kota_kabupaten_id_6`),
  ADD KEY `rokok_by_program_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `rokok_by_program_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `rokok_by_program_perokok_umur_10_sd_18_tahun_idx` (`perokok_umur_10_sd_18_tahun`),
  ADD KEY `rokok_by_program_perokok_umur_diatas_15_tahun_idx` (`perokok_umur_diatas_15_tahun_19`);

--
-- Indexes for table `rokok_by_program_umur`
--
ALTER TABLE `rokok_by_program_umur`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `rokok_by_program_umur_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `rokok_by_program_umur_kecamatan_id_idx` (`kota_kabupaten_id_6`),
  ADD KEY `rokok_by_program_umur_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `rokok_by_program_umur_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `rokok_by_program_umur_jumlah_umur_10_sd_18_tahun_idx` (`jumlah_umur_10_sd_18_tahun`),
  ADD KEY `rokok_by_program_umur_jumlah_umur_15_sd_18_tahun_idx` (`jumlah_umur_15_sd_18_tahun`),
  ADD KEY `rokok_by_program_umur_jumlah_umur_diatas_15_tahun_idx` (`jumlah_umur_diatas_15_tahun_19`),
  ADD KEY `rokok_by_program_umur_survei_id_idx` (`survei_id`),
  ADD KEY `rokok_by_program_umur_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`),
  ADD KEY `rokok_by_program_umur_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`);

--
-- Indexes for table `sasaran_life_cycle_spm`
--
ALTER TABLE `sasaran_life_cycle_spm`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `slcs_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `slcs_provinsi_id_idx` (`provinsi_id_4`),
  ADD KEY `slcs_survei_id_idx` (`survei_id`),
  ADD KEY `slcs_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id_2`),
  ADD KEY `slcs_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `slcs_usia_≥_60_tahun_idx` (`usia_≥_60_tahun`),
  ADD KEY `slcs_usia_15_sd_59_tahun_idx` (`usia_15_sd_59_tahun`),
  ADD KEY `slcs_usia_7_sd_15_tahun_idx` (`usia_7_sd_15_tahun`),
  ADD KEY `slcs_usia_0_sd_59_bulan_idx` (`usia_0_sd_59_bulan_18`),
  ADD KEY `slcs_hamil_idx` (`hamil`),
  ADD KEY `slcs_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `slcs_kelurahan_id_idx` (`kelurahan_id_10`);

--
-- Indexes for table `tb_paru`
--
ALTER TABLE `tb_paru`
  ADD PRIMARY KEY (`survei_individu_detail_id_1`),
  ADD KEY `tb_paru_survei_id_idx` (`survei_id`),
  ADD KEY `tb_paru_survei_individu_detail_id_idx` (`survei_individu_detail_id_1`),
  ADD KEY `tb_paru_didiagnosis_tapi_tidak_minum_obat_tb_idx` (`didiagnosis_tapi_tidak_minum_obat_tb`),
  ADD KEY `tb_paru_penderita_tb_yang_minum_obat_sesuai_standar_idx` (`penderita_tb_yang_minum_obat_sesuai_standar`),
  ADD KEY `tb_paru_suspek_tb_idx` (`suspek_tb`),
  ADD KEY `tb_paru_didiagnosis_tb_idx` (`didiagnosis_tb`),
  ADD KEY `tb_paru_≥15_tahun_idx` (`≥15_tahun`),
  ADD KEY `tb_paru_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `tb_paru_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `tb_paru_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `tb_paru_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id`);

--
-- Indexes for table `tumbuh_kembang`
--
ALTER TABLE `tumbuh_kembang`
  ADD PRIMARY KEY (`survei_individu_detail_id`),
  ADD KEY `tumbuh_kembang_survei_id_idx` (`survei_id`),
  ADD KEY `tumbuh_kembang_survei_individu_detail_id_idx` (`survei_individu_detail_id`),
  ADD KEY `tumbuh_kembang_sasaran_tidak_pemantauan_pertumbuhan_idx` (`sasaran_tidak_pemantauan_pertumbuhan`),
  ADD KEY `tumbuh_kembang_usia_2_sd_59_bulan_idx` (`usia_2_sd_59_bulan`),
  ADD KEY `tumbuh_kembang_kd_puskesmas_idx` (`kd_puskesmas`),
  ADD KEY `tumbuh_kembang_kelurahan_id_idx` (`kelurahan_id`),
  ADD KEY `tumbuh_kembang_kecamatan_id_idx` (`kota_kabupaten_id`),
  ADD KEY `tumbuh_kembang_provinsi_id_idx` (`provinsi_id`),
  ADD KEY `tumbuh_kembang_survei_rumah_tangga_id_idx` (`survei_rumah_tangga_id_2`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
