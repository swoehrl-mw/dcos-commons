import sdk_utils

OPENSSL_TO_RFC_NAMES = {
    'ADH-AES128-GCM-SHA256': 'TLS_DH_anon_WITH_AES_128_GCM_SHA256',
    'ADH-AES128-SHA': 'TLS_DH_anon_WITH_AES_128_CBC_SHA',
    'ADH-AES128-SHA256': 'TLS_DH_anon_WITH_AES_128_CBC_SHA256',
    'ADH-AES256-GCM-SHA384': 'TLS_DH_anon_WITH_AES_256_GCM_SHA384',
    'ADH-AES256-SHA': 'TLS_DH_anon_WITH_AES_256_CBC_SHA',
    'ADH-AES256-SHA256': 'TLS_DH_anon_WITH_AES_256_CBC_SHA256',
    'ADH-CAMELLIA128-SHA': 'TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA',
    'ADH-CAMELLIA128-SHA256': 'TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256',
    'ADH-CAMELLIA256-SHA': 'TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA',
    'ADH-CAMELLIA256-SHA256': 'TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256',
    'ADH-DES-CBC-SHA': 'TLS_DH_anon_WITH_DES_CBC_SHA',
    'ADH-DES-CBC3-SHA': 'TLS_DH_anon_WITH_3DES_EDE_CBC_SHA',
    'ADH-RC4-MD5': 'TLS_DH_anon_WITH_RC4_128_MD5',
    'ADH-SEED-SHA': 'TLS_DH_anon_WITH_SEED_CBC_SHA',
    'AECDH-AES128-SHA': 'TLS_ECDH_anon_WITH_AES_128_CBC_SHA',
    'AECDH-AES256-SHA': 'TLS_ECDH_anon_WITH_AES_256_CBC_SHA',
    'AECDH-DES-CBC3-SHA': 'TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA',
    'AECDH-NULL-SHA': 'TLS_ECDH_anon_WITH_NULL_SHA',
    'AECDH-RC4-SHA': 'TLS_ECDH_anon_WITH_RC4_128_SHA',
    'AES128-CCM': 'RSA_WITH_AES_128_CCM',
    'AES128-CCM8': 'RSA_WITH_AES_128_CCM_8',
    'AES128-GCM-SHA256': 'TLS_RSA_WITH_AES_128_GCM_SHA256',
    'AES128-SHA': 'TLS_RSA_WITH_AES_128_CBC_SHA',
    'AES128-SHA256': 'TLS_RSA_WITH_AES_128_CBC_SHA256',
    'AES256-CCM': 'RSA_WITH_AES_256_CCM',
    'AES256-CCM8': 'RSA_WITH_AES_256_CCM_8',
    'AES256-GCM-SHA384': 'TLS_RSA_WITH_AES_256_GCM_SHA384',
    'AES256-SHA': 'TLS_RSA_WITH_AES_256_CBC_SHA',
    'AES256-SHA256': 'TLS_RSA_WITH_AES_256_CBC_SHA256',
    'CAMELLIA128-SHA': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA',
    'CAMELLIA128-SHA256': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    'CAMELLIA256-SHA': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA',
    'CAMELLIA256-SHA256': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256',
    'DES-CBC-MD5': 'SSL_CK_DES_64_CBC_WITH_MD5',
    'DES-CBC-SHA': 'TLS_RSA_WITH_DES_CBC_SHA',
    'DES-CBC3-MD5': 'SSL_CK_DES_192_EDE3_CBC_WITH_MD5',
    'DES-CBC3-SHA': 'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
    'DH-DSS-AES128-GCM-SHA256': 'TLS_DH_DSS_WITH_AES_128_GCM_SHA256',
    'DH-DSS-AES128-SHA': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA',
    'DH-DSS-AES128-SHA256': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA256',
    'DH-DSS-AES256-GCM-SHA384': 'TLS_DH_DSS_WITH_AES_256_GCM_SHA384',
    'DH-DSS-AES256-SHA': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA',
    'DH-DSS-AES256-SHA256': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA256',
    'DH-DSS-CAMELLIA128-SHA': 'TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA',
    'DH-DSS-CAMELLIA256-SHA': 'TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA',
    'DH-DSS-DES-CBC-SHA': 'TLS_DH_DSS_WITH_DES_CBC_SHA',
    'DH-DSS-DES-CBC3-SHA': 'TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA',
    'DH-DSS-SEED-SHA': 'TLS_DH_DSS_WITH_SEED_CBC_SHA',
    'DH-RSA-AES128-GCM-SHA256': 'TLS_DH_RSA_WITH_AES_128_GCM_SHA256',
    'DH-RSA-AES128-SHA': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA',
    'DH-RSA-AES128-SHA256': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA256',
    'DH-RSA-AES256-GCM-SHA384': 'TLS_DH_RSA_WITH_AES_256_GCM_SHA384',
    'DH-RSA-AES256-SHA': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA',
    'DH-RSA-AES256-SHA256': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA256',
    'DH-RSA-CAMELLIA128-SHA': 'TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA',
    'DH-RSA-CAMELLIA256-SHA': 'TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA',
    'DH-RSA-DES-CBC-SHA': 'TLS_DH_RSA_WITH_DES_CBC_SHA',
    'DH-RSA-DES-CBC3-SHA': 'TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA',
    'DH-RSA-SEED-SHA': 'TLS_DH_RSA_WITH_SEED_CBC_SHA',
    'DHE-DSS-AES128-GCM-SHA256': 'TLS_DHE_DSS_WITH_AES_128_GCM_SHA256',
    'DHE-DSS-AES128-SHA': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA',
    'DHE-DSS-AES128-SHA256': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA256',
    'DHE-DSS-AES256-GCM-SHA384': 'TLS_DHE_DSS_WITH_AES_256_GCM_SHA384',
    'DHE-DSS-AES256-SHA': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA',
    'DHE-DSS-AES256-SHA256': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA256',
    'DHE-DSS-CAMELLIA128-SHA': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA',
    'DHE-DSS-CAMELLIA128-SHA256': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256',
    'DHE-DSS-CAMELLIA256-SHA': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA',
    'DHE-DSS-CAMELLIA256-SHA256': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256',
    'DHE-DSS-DES-CBC3-SHA': 'TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA',
    'DHE-DSS-RC4-SHA': 'TLS_DHE_DSS_WITH_RC4_128_SHA',
    'DHE-DSS-SEED-SHA': 'TLS_DHE_DSS_WITH_SEED_CBC_SHA',
    'DHE-PSK-3DES-EDE-CBC-SHA': 'DHE_PSK_WITH_3DES_EDE_CBC_SHA',
    'DHE-PSK-AES128-CBC-SHA': 'DHE_PSK_WITH_AES_128_CBC_SHA',
    'DHE-PSK-AES128-CBC-SHA256': 'DHE_PSK_WITH_AES_128_CBC_SHA256',
    'DHE-PSK-AES128-CCM': 'DHE_PSK_WITH_AES_128_CCM',
    'DHE-PSK-AES128-CCM8': 'DHE_PSK_WITH_AES_128_CCM_8',
    'DHE-PSK-AES128-GCM-SHA256': 'DHE_PSK_WITH_AES_128_GCM_SHA256',
    'DHE-PSK-AES256-CBC-SHA': 'DHE_PSK_WITH_AES_256_CBC_SHA',
    'DHE-PSK-AES256-CBC-SHA384': 'DHE_PSK_WITH_AES_256_CBC_SHA384',
    'DHE-PSK-AES256-CCM': 'DHE_PSK_WITH_AES_256_CCM',
    'DHE-PSK-AES256-CCM8': 'DHE_PSK_WITH_AES_256_CCM_8',
    'DHE-PSK-AES256-GCM-SHA384': 'DHE_PSK_WITH_AES_256_GCM_SHA384',
    'DHE-PSK-CAMELLIA128-SHA256': 'DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    'DHE-PSK-CAMELLIA256-SHA384': 'DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    'DHE-PSK-CHACHA20-POLY1305': 'TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256',
    'DHE-PSK-NULL-SHA': 'DHE_PSK_WITH_NULL_SHA',
    'DHE-PSK-NULL-SHA256': 'DHE_PSK_WITH_NULL_SHA256',
    'DHE-PSK-NULL-SHA384': 'DHE_PSK_WITH_NULL_SHA384',
    'DHE-PSK-RC4-SHA': 'DHE_PSK_WITH_RC4_128_SHA',
    'DHE-RSA-AES128-CCM': 'DHE_RSA_WITH_AES_128_CCM',
    'DHE-RSA-AES128-CCM8': 'DHE_RSA_WITH_AES_128_CCM_8',
    'DHE-RSA-AES128-GCM-SHA256': 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256',
    'DHE-RSA-AES128-SHA': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA',
    'DHE-RSA-AES128-SHA256': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA256',
    'DHE-RSA-AES256-CCM': 'DHE_RSA_WITH_AES_256_CCM',
    'DHE-RSA-AES256-CCM8': 'DHE_RSA_WITH_AES_256_CCM_8',
    'DHE-RSA-AES256-GCM-SHA384': 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384',
    'DHE-RSA-AES256-SHA': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA',
    'DHE-RSA-AES256-SHA256': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256',
    'DHE-RSA-CAMELLIA128-SHA': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA',
    'DHE-RSA-CAMELLIA128-SHA256': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    'DHE-RSA-CAMELLIA256-SHA': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA',
    'DHE-RSA-CAMELLIA256-SHA256': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256',
    'DHE-RSA-CHACHA20-POLY1305': 'TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256',
    'DHE-RSA-DES-CBC3-SHA': 'TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA',
    'DHE-RSA-SEED-SHA': 'TLS_DHE_RSA_WITH_SEED_CBC_SHA',
    'ECDH-ECDSA-AES128-GCM-SHA256': 'TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256',
    'ECDH-ECDSA-AES128-SHA': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA',
    'ECDH-ECDSA-AES128-SHA256': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256',
    'ECDH-ECDSA-AES256-GCM-SHA384': 'TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384',
    'ECDH-ECDSA-AES256-SHA': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA',
    'ECDH-ECDSA-AES256-SHA384': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384',
    'ECDH-ECDSA-DES-CBC3-SHA': 'TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA',
    'ECDH-ECDSA-NULL-SHA': 'TLS_ECDH_ECDSA_WITH_NULL_SHA',
    'ECDH-ECDSA-RC4-SHA': 'TLS_ECDH_ECDSA_WITH_RC4_128_SHA',
    'ECDH-RSA-AES128-GCM-SHA256': 'TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256',
    'ECDH-RSA-AES128-SHA': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA',
    'ECDH-RSA-AES128-SHA256': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256',
    'ECDH-RSA-AES256-GCM-SHA384': 'TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384',
    'ECDH-RSA-AES256-SHA': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA',
    'ECDH-RSA-AES256-SHA384': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384',
    'ECDH-RSA-DES-CBC3-SHA': 'TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA',
    'ECDH-RSA-NULL-SHA': 'TLS_ECDH_RSA_WITH_NULL_SHA',
    'ECDH-RSA-RC4-SHA': 'TLS_ECDH_RSA_WITH_RC4_128_SHA',
    'ECDHE-ECDSA-AES128-CCM': 'ECDHE_ECDSA_WITH_AES_128_CCM',
    'ECDHE-ECDSA-AES128-CCM8': 'ECDHE_ECDSA_WITH_AES_128_CCM_8',
    'ECDHE-ECDSA-AES128-GCM-SHA256': 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256',
    'ECDHE-ECDSA-AES128-SHA': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA',
    'ECDHE-ECDSA-AES128-SHA256': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256',
    'ECDHE-ECDSA-AES256-CCM': 'ECDHE_ECDSA_WITH_AES_256_CCM',
    'ECDHE-ECDSA-AES256-CCM8': 'ECDHE_ECDSA_WITH_AES_256_CCM_8',
    'ECDHE-ECDSA-AES256-GCM-SHA384': 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384',
    'ECDHE-ECDSA-AES256-SHA': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA',
    'ECDHE-ECDSA-AES256-SHA384': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384',
    'ECDHE-ECDSA-CAMELLIA128-SHA256': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256',
    'ECDHE-ECDSA-CAMELLIA256-SHA384': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384',
    'ECDHE-ECDSA-CHACHA20-POLY1305': 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256',
    'ECDHE-ECDSA-DES-CBC3-SHA': 'TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA',
    'ECDHE-ECDSA-NULL-SHA': 'TLS_ECDHE_ECDSA_WITH_NULL_SHA',
    'ECDHE-ECDSA-RC4-SHA': 'TLS_ECDHE_ECDSA_WITH_RC4_128_SHA',
    'ECDHE-PSK-3DES-EDE-CBC-SHA': 'ECDHE_PSK_WITH_3DES_EDE_CBC_SHA',
    'ECDHE-PSK-AES128-CBC-SHA': 'ECDHE_PSK_WITH_AES_128_CBC_SHA',
    'ECDHE-PSK-AES128-CBC-SHA256': 'ECDHE_PSK_WITH_AES_128_CBC_SHA256',
    'ECDHE-PSK-AES256-CBC-SHA': 'ECDHE_PSK_WITH_AES_256_CBC_SHA',
    'ECDHE-PSK-AES256-CBC-SHA384': 'ECDHE_PSK_WITH_AES_256_CBC_SHA384',
    'ECDHE-PSK-CAMELLIA128-SHA256': 'ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    'ECDHE-PSK-CAMELLIA256-SHA384': 'ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    'ECDHE-PSK-CHACHA20-POLY1305': 'TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256',
    'ECDHE-PSK-NULL-SHA': 'ECDHE_PSK_WITH_NULL_SHA',
    'ECDHE-PSK-NULL-SHA256': 'ECDHE_PSK_WITH_NULL_SHA256',
    'ECDHE-PSK-NULL-SHA384': 'ECDHE_PSK_WITH_NULL_SHA384',
    'ECDHE-PSK-RC4-SHA': 'ECDHE_PSK_WITH_RC4_128_SHA',
    'ECDHE-RSA-AES128-GCM-SHA256': 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256',
    'ECDHE-RSA-AES128-SHA': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA',
    'ECDHE-RSA-AES128-SHA256': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256',
    'ECDHE-RSA-AES256-GCM-SHA384': 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384',
    'ECDHE-RSA-AES256-SHA': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA',
    'ECDHE-RSA-AES256-SHA384': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384',
    'ECDHE-RSA-CAMELLIA128-SHA256': 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    'ECDHE-RSA-CAMELLIA256-SHA384': 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384',
    'ECDHE-RSA-CHACHA20-POLY1305': 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256',
    'ECDHE-RSA-DES-CBC3-SHA': 'TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA',
    'ECDHE-RSA-NULL-SHA': 'TLS_ECDHE_RSA_WITH_NULL_SHA',
    'ECDHE-RSA-RC4-SHA': 'TLS_ECDHE_RSA_WITH_RC4_128_SHA',
    'EDH-DSS-DES-CBC-SHA': 'TLS_DHE_DSS_WITH_DES_CBC_SHA',
    'EDH-DSS-DES-CBC3-SHA': 'TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA',
    'EDH-RSA-DES-CBC-SHA': 'TLS_DHE_RSA_WITH_DES_CBC_SHA',
    'EDH-RSA-DES-CBC3-SHA': 'TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA',
    'EXP-ADH-DES-CBC-SHA': 'TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-ADH-RC4-MD5': 'TLS_DH_anon_EXPORT_WITH_RC4_40_MD5',
    'EXP-DES-CBC-SHA': 'TLS_RSA_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-DH-DSS-DES-CBC-SHA': 'TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-DH-RSA-DES-CBC-SHA': 'TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-EDH-DSS-DES-CBC-SHA': 'TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-EDH-RSA-DES-CBC-SHA': 'TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA',
    'EXP-KRB5-DES-CBC-MD5': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5',
    'EXP-KRB5-DES-CBC-SHA': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA',
    'EXP-KRB5-RC2-CBC-MD5': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5',
    'EXP-KRB5-RC2-CBC-SHA': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA',
    'EXP-KRB5-RC4-MD5': 'TLS_KRB5_EXPORT_WITH_RC4_40_MD5',
    'EXP-KRB5-RC4-SHA': 'TLS_KRB5_EXPORT_WITH_RC4_40_SHA',
    'EXP-RC2-CBC-MD5': 'SSL_CK_RC2_128_CBC_EXPORT40_WITH_MD5',
    'EXP-RC2-CBC-MD5': 'TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5',
    'EXP-RC4-MD5': 'SSL_CK_RC4_128_EXPORT40_WITH_MD5',
    'EXP-RC4-MD5': 'TLS_RSA_EXPORT_WITH_RC4_40_MD5',
    'EXP1024-DES-CBC-SHA': 'TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA',
    'EXP1024-DHE-DSS-DES-CBC-SHA': 'TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA',
    'EXP1024-DHE-DSS-RC4-SHA': 'TLS_DHE_DSS_EXPORT1024_WITH_RC4_56_SHA',
    'EXP1024-RC4-SHA': 'TLS_RSA_EXPORT1024_WITH_RC4_56_SHA',
    'GOST2001-GOST89-GOST89': 'TLS_GOSTR341001_WITH_28147_CNT_IMIT',
    'GOST94-GOST89-GOST89': 'TLS_GOSTR341094_WITH_28147_CNT_IMIT',
    'GOST94-NULL-GOST94': 'TLS_GOSTR341094_WITH_NULL_GOSTR3411',
    'IDEA-CBC-MD5': 'SSL_CK_IDEA_128_CBC_WITH_MD5',
    'IDEA-CBC-SHA': 'TLS_RSA_WITH_IDEA_CBC_SHA',
    'KRB5-DES-CBC-MD5': 'TLS_KRB5_WITH_DES_CBC_MD5',
    'KRB5-DES-CBC-SHA': 'TLS_KRB5_WITH_DES_CBC_SHA',
    'KRB5-DES-CBC3-MD5': 'TLS_KRB5_WITH_3DES_EDE_CBC_MD5',
    'KRB5-DES-CBC3-SHA': 'TLS_KRB5_WITH_3DES_EDE_CBC_SHA',
    'KRB5-IDEA-CBC-MD5': 'TLS_KRB5_WITH_IDEA_CBC_MD5',
    'KRB5-IDEA-CBC-SHA': 'TLS_KRB5_WITH_IDEA_CBC_SHA',
    'KRB5-RC4-MD5': 'TLS_KRB5_WITH_RC4_128_MD5',
    'KRB5-RC4-SHA': 'TLS_KRB5_WITH_RC4_128_SHA',
    'NULL-MD5': 'TLS_NULL_WITH_NULL_NULL',
    'NULL-MD5': 'TLS_RSA_WITH_NULL_MD5',
    'NULL-SHA': 'TLS_RSA_WITH_NULL_SHA',
    'NULL-SHA256': 'TLS_RSA_WITH_NULL_SHA256',
    'PSK-3DES-EDE-CBC-SHA': 'TLS_PSK_WITH_3DES_EDE_CBC_SHA',
    'PSK-AES128-CBC-SHA': 'TLS_PSK_WITH_AES_128_CBC_SHA',
    'PSK-AES128-CBC-SHA256': 'PSK_WITH_AES_128_CBC_SHA256',
    'PSK-AES128-CCM': 'PSK_WITH_AES_128_CCM',
    'PSK-AES128-CCM8': 'PSK_WITH_AES_128_CCM_8',
    'PSK-AES128-GCM-SHA256': 'PSK_WITH_AES_128_GCM_SHA256',
    'PSK-AES128-GCM-SHA256': 'PSK_WITH_AES_128_GCM_SHA256',
    'PSK-AES256-CBC-SHA': 'TLS_PSK_WITH_AES_256_CBC_SHA',
    'PSK-AES256-CBC-SHA384': 'PSK_WITH_AES_256_CBC_SHA384',
    'PSK-AES256-CCM': 'PSK_WITH_AES_256_CCM',
    'PSK-AES256-CCM8': 'PSK_WITH_AES_256_CCM_8',
    'PSK-AES256-GCM-SHA384': 'PSK_WITH_AES_256_GCM_SHA384',
    'PSK-AES256-GCM-SHA384': 'PSK_WITH_AES_256_GCM_SHA384',
    'PSK-CAMELLIA128-SHA256': 'PSK_WITH_CAMELLIA_128_CBC_SHA256',
    'PSK-CAMELLIA256-SHA384': 'PSK_WITH_CAMELLIA_256_CBC_SHA384',
    'PSK-CHACHA20-POLY1305': 'TLS_PSK_WITH_CHACHA20_POLY1305_SHA256',
    'PSK-NULL-SHA': 'PSK_WITH_NULL_SHA',
    'PSK-NULL-SHA256': 'PSK_WITH_NULL_SHA256',
    'PSK-NULL-SHA384': 'PSK_WITH_NULL_SHA384',
    'PSK-RC4-SHA': 'TLS_PSK_WITH_RC4_128_SHA',
    'RC2-CBC-MD5': 'SSL_CK_RC2_128_CBC_WITH_MD5',
    'RC4-64-MD5': 'SSL_CK_RC4_64_WITH_MD5',
    'RC4-MD5': 'TLS_RSA_WITH_RC4_128_MD5',
    'RC4-SHA': 'TLS_RSA_WITH_RC4_128_SHA',
    'RSA-PSK-3DES-EDE-CBC-SHA': 'RSA_PSK_WITH_3DES_EDE_CBC_SHA',
    'RSA-PSK-AES128-CBC-SHA': 'RSA_PSK_WITH_AES_128_CBC_SHA',
    'RSA-PSK-AES128-CBC-SHA256': 'RSA_PSK_WITH_AES_128_CBC_SHA256',
    'RSA-PSK-AES128-GCM-SHA256': 'RSA_PSK_WITH_AES_128_GCM_SHA256',
    'RSA-PSK-AES256-CBC-SHA': 'RSA_PSK_WITH_AES_256_CBC_SHA',
    'RSA-PSK-AES256-CBC-SHA384': 'RSA_PSK_WITH_AES_256_CBC_SHA384',
    'RSA-PSK-AES256-GCM-SHA384': 'RSA_PSK_WITH_AES_256_GCM_SHA384',
    'RSA-PSK-CAMELLIA128-SHA256': 'RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    'RSA-PSK-CAMELLIA256-SHA384': 'RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    'RSA-PSK-CHACHA20-POLY1305': 'TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256',
    'RSA-PSK-NULL-SHA': 'RSA_PSK_WITH_NULL_SHA',
    'RSA-PSK-NULL-SHA256': 'RSA_PSK_WITH_NULL_SHA256',
    'RSA-PSK-NULL-SHA384': 'RSA_PSK_WITH_NULL_SHA384',
    'RSA-PSK-RC4-SHA': 'RSA_PSK_WITH_RC4_128_SHA',
    'SEED-SHA': 'TLS_RSA_WITH_SEED_CBC_SHA',
    'SRP-3DES-EDE-CBC-SHA': 'TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA',
    'SRP-AES-128-CBC-SHA': 'TLS_SRP_SHA_WITH_AES_128_CBC_SHA',
    'SRP-AES-256-CBC-SHA': 'TLS_SRP_SHA_WITH_AES_256_CBC_SHA',
    'SRP-DSS-3DES-EDE-CBC-SHA': 'TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA',
    'SRP-DSS-AES-128-CBC-SHA': 'TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA',
    'SRP-DSS-AES-256-CBC-SHA': 'TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA',
    'SRP-RSA-3DES-EDE-CBC-SHA': 'TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA',
    'SRP-RSA-AES-128-CBC-SHA': 'TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA',
    'SRP-RSA-AES-256-CBC-SHA': 'TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA',
    'TLS_FALLBACK_SCSV': 'TLS_FALLBACK_SCSV'
}

RFC_TO_OPENSSL_NAMES = sdk_utils.invert_dict(OPENSSL_TO_RFC_NAMES)


def missing_ciphers(openssl_ciphers: set) -> bool:
    """Returns the OpenSSL ciphers absent from OPENSSL_TO_RFC_NAMES.
    """
    return openssl_ciphers - set(OPENSSL_TO_RFC_NAMES.keys())


def rfc_name(openssl_name: str) -> str:
    return OPENSSL_TO_RFC_NAMES.get(openssl_name)


def openssl_name(rfc_name: str) -> str:
    return RFC_TO_OPENSSL_NAMES.get(rfc_name)
