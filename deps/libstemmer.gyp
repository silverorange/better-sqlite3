# ===
# This configuration defines options specific to compiling libstemmer.
# Before libstemmer is compiled, it gets downloaded from github, extracted
# and has its C source code generated.
# ===
{
  'includes': ['common.gypi'],
  'targets': [
    {
      'target_name': 'download_libstemmer',
      'type': 'none',
      'hard_dependency': 1,
      'actions': [
        {
          'action_name': 'download_libstemmer_action',
          'inputs': [],
          'outputs': ['<(SHARED_INTERMEDIATE_DIR)/libstemmer/snowball-<(LIBSTEMMER_VERSION).tar.gz'],
          'action': ['node', 'libstemmer_download.js', '<(LIBSTEMMER_VERSION)', '<(SHARED_INTERMEDIATE_DIR)/libstemmer'],
        }
      ],
    },
    {
      'target_name': 'build_libstemmer_src',
      'type': 'none',
      'dependencies': ['download_libstemmer'],
      'hard_dependency': 1,
      'actions': [
        {
          'action_name': 'build_libstemmer_src_action',
          'inputs': [],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/libstemmer/dist/libstemmer_c-<(LIBSTEMMER_VERSION).tar.gz',
          ],
          'action': ['node', 'libstemmer_build_source.js', '<(LIBSTEMMER_VERSION)', '<(SHARED_INTERMEDIATE_DIR)/libstemmer'],
        }
      ],
    },
    {
      'target_name': 'libstemmer',
      'type': 'static_library',
      'dependencies': ['build_libstemmer_src'],
      'sources': [
        # There is a mysterious bug in gyp where it will not build files from
        # the first directory containing source files during the invocation of
        # node-gyp. To work around this issue we include this shim file that is
        # not part of the generated output of another build step.
        'libstemmer_gyp_shim.c',
        # Google says you have to list all these files manually, even if they
        # are generated: https://groups.google.com/g/gyp-developer/c/rEB2aHf9Dbg
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/libstemmer/libstemmer.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/runtime/utilities.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/runtime/api.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_basque.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_catalan.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_danish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_dutch.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_english.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_finnish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_french.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_german.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_indonesian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_irish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_italian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_norwegian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_porter.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_portuguese.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_spanish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_1_swedish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_2_hungarian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_ISO_8859_2_romanian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_KOI8_R_russian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_arabic.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_armenian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_basque.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_catalan.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_danish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_dutch.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_english.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_finnish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_french.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_german.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_greek.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_hindi.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_hungarian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_indonesian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_irish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_italian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_lithuanian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_nepali.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_norwegian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_porter.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_portuguese.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_romanian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_russian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_serbian.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_spanish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_swedish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_tamil.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_turkish.c',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c/stem_UTF_8_yiddish.c',
      ],
      'include_dirs': [
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/include',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/libstemmer',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/runtime',
        '<(SHARED_INTERMEDIATE_DIR)/libstemmer/src_c',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)/libstemmer/include',
        ],
      },
      'cflags': ['-std=c99', '-w'],
      'xcode_settings': {
        'OTHER_CFLAGS': ['-std=c99'],
        'WARNING_CFLAGS': ['-w'],
      },
      'configurations': {
        'Debug': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 1 } }, # static debug
        },
        'Release': {
          'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 0 } }, # static release
        },
      },
    },
  ],
}
