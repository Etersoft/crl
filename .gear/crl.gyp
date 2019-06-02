# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'targets': [{
    'target_name': 'libcrl',
    'type': 'shared_library',
    'product_extension': 'so.0.8',
    'dependencies': [],
    'link_settings': { 'libraries': ['-lQt5Core'] },
    'defines': [
    ],
    'variables': {
      'crl_src_loc': './src/crl',
      'official_build_target%': ''
    },
    'include_dirs': [
      './src',
    ],
    'sources': [
      '<(crl_src_loc)/common/crl_common_config.h',
      '<(crl_src_loc)/common/crl_common_list.cpp',
      '<(crl_src_loc)/common/crl_common_list.h',
      '<(crl_src_loc)/common/crl_common_on_main.cpp',
      '<(crl_src_loc)/common/crl_common_on_main.h',
      '<(crl_src_loc)/common/crl_common_on_main_guarded.h',
      '<(crl_src_loc)/common/crl_common_queue.cpp',
      '<(crl_src_loc)/common/crl_common_queue.h',
      '<(crl_src_loc)/common/crl_common_sync.h',
      '<(crl_src_loc)/common/crl_common_utils.h',
      '<(crl_src_loc)/dispatch/crl_dispatch_async.cpp',
      '<(crl_src_loc)/dispatch/crl_dispatch_async.h',
      '<(crl_src_loc)/dispatch/crl_dispatch_on_main.h',
      '<(crl_src_loc)/dispatch/crl_dispatch_queue.cpp',
      '<(crl_src_loc)/dispatch/crl_dispatch_queue.h',
      '<(crl_src_loc)/dispatch/crl_dispatch_semaphore.cpp',
      '<(crl_src_loc)/dispatch/crl_dispatch_semaphore.h',
      '<(crl_src_loc)/mac/crl_mac_time.cpp',
      '<(crl_src_loc)/linux/crl_linux_time.cpp',
      '<(crl_src_loc)/qt/crl_qt_async.cpp',
      '<(crl_src_loc)/qt/crl_qt_async.h',
      '<(crl_src_loc)/qt/crl_qt_semaphore.cpp',
      '<(crl_src_loc)/qt/crl_qt_semaphore.h',
      '<(crl_src_loc)/winapi/crl_winapi_async.cpp',
      '<(crl_src_loc)/winapi/crl_winapi_async.h',
      '<(crl_src_loc)/winapi/crl_winapi_dll.h',
      '<(crl_src_loc)/winapi/crl_winapi_list.cpp',
      '<(crl_src_loc)/winapi/crl_winapi_list.h',
      '<(crl_src_loc)/winapi/crl_winapi_semaphore.cpp',
      '<(crl_src_loc)/winapi/crl_winapi_semaphore.h',
      '<(crl_src_loc)/winapi/crl_winapi_time.cpp',
      '<(crl_src_loc)/crl.h',
      '<(crl_src_loc)/crl_async.h',
      '<(crl_src_loc)/crl_object_on_queue.h',
      '<(crl_src_loc)/crl_on_main.h',
      '<(crl_src_loc)/crl_queue.h',
      '<(crl_src_loc)/crl_semaphore.h',
      '<(crl_src_loc)/crl_time.cpp',
      '<(crl_src_loc)/crl_time.h',
    ],
  }],
}
