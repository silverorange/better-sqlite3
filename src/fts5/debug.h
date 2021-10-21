#ifndef DEBUG_H
#define DEBUG_H

#ifdef SQLC_KEEP_ANDROID_LOG
#define log_error(...) __android_log_print(ANDROID_LOG_VERBOSE, "sqlc-tokenizers", __VA_ARGS__)
#define log_debug(...) __android_log_print(ANDROID_LOG_VERBOSE, "sqlc-tokenizers", __VA_ARGS__)
#define SQLITE_TOKENIZER_DEBUG 1
#elif defined SQLITE_TOKENIZER_DEBUG
#include <stdio.h>
#define log_error(...) fprintf(stderr, __VA_ARGS__)
#define log_debug(...) printf(__VA_ARGS__)
#else
#define log_error(...)
#define log_debug(...)
#endif

#endif
