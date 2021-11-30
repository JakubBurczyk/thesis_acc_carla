import collections
import bisect


class LUT_brake_distance():
    def __init__(self):
        self.table = collections.OrderedDict()
        self.table = {0.012:0,0.17:0,0.214:0.002,0.343:0.002,0.475:0.003,0.601:0.004,0.729:0.015,0.858:0.017,0.984:0.023,1.098:0.027,
            1.225:0.029,1.357:0.032,1.475:0.037,1.609:0.043,1.729:0.048,1.86:0.057,1.984:0.063,2.113:0.073,2.239:0.1,2.368:0.134,
            2.494:0.156,2.622:0.159,2.749:0.169,2.877:0.186,3.003:0.189,3.132:0.195,3.257:0.202,3.314:0.251,3.43:0.258,3.512:0.278,
            3.611:0.286,3.634:0.289,3.718:0.308,3.765:0.326,3.833:0.334,3.891:0.396,3.954:0.404,4.015:0.427,4.077:0.444,4.138:0.452,
            4.199:0.46,4.261:0.481,4.322:0.541,4.384:0.546,4.445:0.572,4.507:0.581,4.568:0.604,4.63:0.608,4.692:0.632,4.753:0.637,
            4.815:0.651,4.877:0.656,4.938:0.666,5:0.685,5.062:0.695,5.124:0.695,5.185:0.716,5.247:0.82,5.309:0.873,5.371:0.884,
            5.433:0.895,5.494:0.922,5.556:0.933,5.618:0.944,5.68:0.95,5.742:0.996,5.804:1.007,5.866:1.03,5.928:1.036,5.99:1.102,
            6.052:1.108,6.114:1.12,6.176:1.132,6.238:1.17,6.3:1.182,6.362:1.321,6.425:1.328,6.487:1.367,6.549:1.373,6.611:1.386,
            6.673:1.419,6.736:1.493,6.798:1.5,6.86:1.507,6.922:1.541,6.985:1.548,7.047:1.618,7.109:1.767,7.172:2.045,7.234:2.06,
            7.297:2.089,7.359:2.104,7.421:2.148,7.484:2.312,7.546:3.018,7.609:3.033,7.671:3.033,7.734:3.072,7.796:3.088,7.859:3.103,
            7.922:3.143,7.984:3.151,8.047:3.175,8.11:3.199,8.172:3.24,8.235:3.248,8.298:3.256,8.36:3.306,8.423:3.323,8.486:3.34,
            8.549:3.348,8.612:3.425,8.674:3.434,8.737:3.469,8.8:3.486,8.863:3.548,8.926:3.566,8.989:3.584,9.052:3.602,9.115:3.638,
            9.178:3.675,9.241:3.739,9.304:3.758,9.367:3.786,9.43:3.974,9.493:4.021,9.556:4.031,9.619:4.069,9.682:4.088,9.745:4.098,
            9.809:4.137,9.872:4.157,9.935:4.276,9.998:4.276,10.062:4.306,10.125:4.326,10.188:4.336,10.251:4.367,10.315:4.387,10.378:4.491,
            10.442:4.522,10.505:4.574,10.568:4.585,10.632:4.585,10.695:4.681,10.759:4.702,10.822:4.746,10.886:4.767,10.949:4.8,11.013:4.866,
            11.076:4.877,11.14:4.888,11.204:4.922,11.267:5.158,11.331:5.214,11.395:5.237,11.458:5.271,11.522:5.294,11.586:5.363,11.649:5.375,
            11.713:5.445,11.777:5.457,11.841:5.469,11.905:5.528,11.968:5.552,12.032:5.588,12.096:5.636,12.16:5.842,12.224:5.867,12.288:5.891,
            12.352:5.928,12.416:5.953,12.48:5.978,12.544:6.053,12.608:6.116,12.672:6.179,12.736:6.204,12.8:6.217,12.864:6.256,12.929:6.269,
            12.993:6.605,13.057:6.684,13.121:6.723,13.185:6.749,13.25:6.776,13.314:6.815,13.378:6.896,13.443:6.922,13.507:7.259,13.571:8.491,
            13.636:9.117,13.7:9.144,13.764:9.199,13.829:9.213,13.893:9.241,13.958:9.269,14.022:9.297,14.087:9.311,14.151:9.381,14.216:9.41,
            14.281:9.438,14.345:9.596,14.41:9.711,14.474:9.725,14.539:9.74,14.604:9.798,14.668:9.798,14.733:9.989,14.798:10.019,14.863:10.122,
            14.927:10.137,14.992:10.167,15.057:10.197,15.122:10.227,15.187:10.288,15.252:10.379,15.317:10.425,15.381:10.625,15.446:10.64,15.511:10.656,
            15.576:10.78,15.641:10.811,15.706:10.858,15.771:10.858,15.836:10.89,15.902:11.049,15.967:11.064,16.032:11.096,16.097:11.145,16.162:11.338,
            16.227:11.419,16.293:11.435,16.358:11.468,16.423:11.55,16.488:11.566,16.554:11.765,16.619:11.798,16.684:11.831,16.75:11.965,16.815:11.982,
            16.88:12.015,16.946:12.032,17.011:12.032,17.077:12.237,17.142:12.237,17.208:12.271,17.273:12.34,17.339:12.427,17.404:12.618,17.47:12.635,
            17.536:12.775,17.601:12.793,17.667:12.952,17.733:13.04,17.798:13.076,17.864:13.2,17.93:13.218,17.995:13.254,18.061:13.272,18.127:13.29,
            18.193:13.472,18.259:13.49,18.325:13.508,18.39:13.729,18.456:13.784,18.522:13.802,18.588:13.821,18.654:13.896,18.72:13.933,18.786:13.952,
            18.852:14.027,18.918:14.065,18.984:14.065,19.05:14.141,19.117:14.16,19.183:14.217,19.249:14.256,19.315:14.333,19.381:14.372,19.447:14.566,
            19.514:14.605,19.58:14.859,19.646:14.898,19.713:14.996,19.779:15.036,19.845:15.076,19.912:15.175,19.978:15.275,20.044:15.275,20.111:15.315,
            20.177:15.335,20.244:15.638,20.31:15.699,20.377:15.74,20.443:15.862,20.51:15.903,20.577:15.965,20.643:15.965,20.71:16.006,20.776:16.255,
            20.843:16.276,20.91:16.297,20.977:16.464,21.043:16.506,21.11:16.569,21.177:16.612,21.244:16.675,21.31:16.718,21.377:16.825,21.444:16.825,
            21.511:16.868,21.578:16.889,21.645:16.954,21.712:16.954,21.779:16.997,21.846:17.194,21.913:17.303,21.98:17.435,22.047:17.479,22.114:17.501,
            22.181:17.545,22.248:17.701,22.315:18.124,22.383:18.146,22.45:18.214,22.517:18.236,22.584:18.304,22.652:18.394,22.719:18.417,22.786:18.644,
            22.854:18.69,22.921:18.805,22.988:18.965,23.056:18.965,23.123:19.011,23.19:19.081,23.258:19.104,23.325:19.36,23.393:19.384,23.46:19.454,
            23.528:19.665,23.596:19.713,23.663:19.76,23.731:19.807,23.798:20.14,23.866:20.307,23.934:20.331,24.001:20.331,24.069:20.403,24.137:20.62,
            24.205:20.765,24.273:20.765,24.34:21.056,24.408:21.105,24.476:21.13,24.544:21.301,24.612:21.35,24.68:21.424,24.748:21.474,24.816:21.498,
            24.884:21.548,24.952:21.573,25.02:21.648,25.088:21.698,25.156:21.799,25.224:21.824,25.292:22.127,25.36:22.355,25.428:22.355,25.497:22.406,
            25.565:22.431,25.633:22.482,25.701:22.79,25.77:22.816,25.838:22.868,25.906:22.945,25.975:23.101,26.043:23.205,26.111:23.257,26.18:23.545,
            26.248:23.597,26.317:23.702,26.385:23.729,26.454:23.782,26.522:24.02,26.591:24.232,26.66:24.738,26.728:25.966,26.797:26.154,26.865:26.261,
            26.934:26.342,27.003:26.476,27.071:26.693,27.14:26.747,27.209:26.856,27.278:26.992,27.347:27.046,27.415:27.074,27.484:27.129,27.553:27.211,
            27.622:27.322,27.691:27.349,27.76:27.46,27.829:27.516,27.898:27.683,27.967:27.739,28.036:27.739,28.105:27.823,28.174:28.161,28.243:28.697,
            28.312:28.697,28.382:28.725,28.451:28.81,28.52:28.981,28.589:29.038,28.658:29.181,28.728:29.239,28.797:29.268,28.866:29.498,28.936:29.556,
            29.005:29.73,29.074:29.817,29.144:29.846,29.213:29.875,29.283:30.051,29.352:30.725,29.422:30.784,29.491:30.813,29.561:31.05,29.63:31.079,
            29.7:31.138,29.77:31.376,29.839:31.823,29.909:31.883,29.979:31.973,30.048:32.033,30.118:32.093,30.188:32.636,30.258:32.878,30.327:33.271,
            30.397:33.484,30.467:34.184,30.537:34.275,30.607:34.428,30.677:34.643,30.747:34.674,30.817:34.797,30.887:34.828,30.957:35.26,31.027:35.291,
            31.097:35.416,31.167:35.478,31.237:35.54,31.307:35.916,31.377:36.041,31.448:36.167,31.518:36.23,31.588:36.356,31.658:36.356,31.729:36.451,
            31.799:36.483,31.869:36.705,31.94:36.833,32.01:37.025,32.08:37.089,32.151:37.153,32.221:37.829,32.292:38.023,32.362:38.217,32.433:38.249,
            32.503:38.379,32.574:38.411,32.644:38.477,32.715:38.607,32.786:38.64,32.856:38.706,32.927:38.903,32.998:39.068,33.068:39.134,33.139:39.167,
            33.21:39.399,33.281:39.632,33.352:39.699,33.422:39.732,33.493:39.799,33.564:40.034,33.635:40.168,33.706:40.235,33.777:40.438,33.848:40.641,
            33.919:40.709,33.99:40.81,34.061:41.457,34.132:41.627,34.204:41.627,34.275:41.662,34.346:42.073,34.417:42.108,34.488:42.142,34.56:42.384,
            34.631:42.384,34.702:42.592,34.773:42.661,34.845:42.731,34.916:42.801,34.988:42.871,35.059:43.151,35.13:43.467,35.202:43.537,35.273:43.713,
            35.345:43.819,35.416:43.854,35.488:43.925,35.56:44.21,35.631:44.53,35.703:44.566,35.774:44.637,35.846:44.709,35.918:44.852,35.99:45.679,
            36.061:45.715,36.133:45.751,36.205:45.751,36.277:45.969,36.349:46.041,36.421:46.114,36.492:46.151,36.564:46.37,36.636:46.48,36.708:46.553,
            36.78:46.81,36.852:47.252,36.924:47.252,36.996:47.326,37.069:47.622,37.141:47.659,37.213:47.771,37.285:47.808,37.357:47.957,37.43:47.995,
            37.502:48.144,37.574:48.22,37.646:48.257,37.719:48.446,37.791:48.483,37.863:48.559,37.936:48.824,38.008:48.938,38.081:49.395,38.153:49.814,
            38.226:49.89,38.298:49.929,38.371:50.235,38.443:50.312,38.516:50.428,38.589:50.466,38.661:50.582,38.734:50.621,38.807:50.66,38.879:50.815,
            38.952:51.204,39.025:51.243,39.098:51.321,39.171:51.791,39.244:51.83,39.316:51.948,39.389:51.948,39.462:52.224,39.535:52.224,39.608:52.263,
            39.681:52.937,39.754:53.096,39.827:53.176,39.9:53.255,39.974:53.295,40.047:53.375,40.12:53.616,40.193:53.696,40.266:54.099,40.34:54.139,
            40.413:54.341,40.486:54.503,40.559:54.584,40.633:54.665,40.706:55.397,40.78:55.478,40.853:55.682,40.926:55.682,41:55.805,41.073:55.928,
            41.147:56.052,41.22:56.299,41.294:56.546,41.368:56.629,41.441:56.753,41.515:57.624,41.589:57.79,41.662:57.832,41.736:57.916,41.81:58.375,
            41.884:58.417,41.957:58.459,42.031:58.585,42.105:58.879,42.179:59.132,42.253:59.217,42.327:59.301,42.401:59.386,42.475:60.107,42.549:60.15,
            42.623:60.405,42.697:60.661,42.771:60.747,42.845:60.918,42.919:60.961,42.993:61.39,43.068:61.433,43.142:61.52,43.216:61.606,43.29:62.471,
            43.365:62.731,43.439:62.818,43.513:62.818,43.588:62.905,43.662:63.167,43.737:63.254,43.811:63.473,43.886:63.517,43.96:63.649,44.035:64.045,
            44.109:64.133,44.184:64.265,44.259:64.575,44.333:64.619,44.408:65.151,44.483:65.64,44.557:65.729,44.632:66.265,44.707:66.354,44.782:66.443,
            44.856:67.564,44.931:68.147,45.006:68.192,45.081:68.328,45.156:68.373,45.231:68.779,45.306:68.825,45.381:68.915,45.456:69.006,45.531:69.279,
            45.606:69.963,45.681:70.1,45.757:70.191,45.832:70.237,45.907:70.42,45.982:70.512,46.057:70.696,46.133:70.788,46.208:71.435,46.283:71.481,
            46.359:71.805,46.434:71.898,46.51:71.991,46.585:72.084,46.66:72.177,46.736:72.411,46.812:72.458,46.887:72.692,46.963:72.833,47.038:73.256,
            47.114:73.303,47.19:73.35,47.265:73.869,47.341:74.863,47.417:74.863,47.493:75.005,47.568:75.243,47.644:75.338,47.72:75.433,47.796:75.624,
            47.872:75.864,47.948:75.912,48.024:76.007,48.1:76.152,48.176:76.248,48.252:76.393,48.328:77.02,48.404:77.407,48.48:77.456,48.556:77.553,
            48.632:77.65,48.709:77.893,48.785:78.137,48.861:78.235,48.937:78.577,49.014:79.067,49.09:79.165,49.166:79.361,49.243:79.706,49.319:80.051,
            49.396:80.89,49.472:80.989,49.549:81.236,49.625:81.286,49.702:81.832,49.778:81.932,49.855:82.081,49.932:82.38,50.008:82.53,50.085:82.781,
            50.162:83.282,50.238:83.683,50.315:83.885,50.392:84.237,50.469:84.64,50.546:84.842,50.623:84.944,50.7:85.248,50.777:85.298,50.854:85.451,
            50.931:85.502,51.008:86.317,51.085:86.623,51.162:86.675,51.239:86.931,51.316:87.033,51.393:87.495,51.47:87.598,51.548:87.701,51.625:87.856,
            51.702:88.114,51.779:88.218,51.857:88.27,51.934:88.529,52.011:88.581,52.089:89.258,52.166:89.362,52.244:89.675,52.321:89.78,52.399:89.884,
            52.476:90.042,52.554:90.199,52.632:90.673,52.709:90.778,52.787:91.094,52.865:91.147,52.942:91.253,53.02:91.359,53.098:92.42,53.176:93.164,
            53.254:93.164,53.331:93.271,53.409:93.431,53.487:93.645,53.565:93.805,53.643:94.02,53.721:94.073,53.799:94.288,53.877:94.288,53.955:94.558,
            54.033:94.666,54.111:94.882,54.19:94.936,54.268:95.045,54.346:95.914,54.424:96.077,54.503:96.567,54.581:99.24,54.659:99.458,54.738:99.622,
            54.816:99.896,54.894:100.225,54.973:100.72,55.051:100.83,55.13:101.05,55.208:101.216,55.287:101.713,55.365:102.432,55.444:102.543,55.523:102.82,
            55.601:103.431,55.68:103.598,55.759:103.765,55.837:104.1,55.916:104.212,55.995:104.268,56.074:104.604,56.153:105.221,56.232:105.278,56.311:105.334,
            56.389:105.785,56.468:105.841,56.547:106.011,56.626:106.124,56.705:106.407,56.785:106.521,56.864:106.748,56.943:106.919,57.022:107.318,57.101:107.432,
            57.18:107.546,57.259:107.603,57.339:108.577,57.418:108.921,57.497:109.151,57.577:109.554,57.656:110.764,57.735:110.937,57.815:111.457,57.894:112.209,
            57.974:112.499,58.053:112.557,58.133:112.615,58.212:112.848,58.292:112.964,58.371:113.722,58.451:113.781,58.531:114.132,58.61:114.308,58.69:114.425,
            58.77:114.953,58.85:115.071,58.929:115.365,59.009:115.365,59.089:115.484,59.169:115.602,59.249:115.661,59.329:115.78,59.409:115.958,59.489:116.79,
            59.569:117.802,59.649:118.04,59.729:118.697,59.809:118.936,59.889:119.056,59.969:119.775,60.049:120.195,60.129:120.435,60.209:121.157,60.29:121.941,
            60.37:122.122,60.45:122.303,60.53:122.484,60.611:122.787,60.691:123.394,60.771:123.819,60.852:124.062,60.932:125.28,61.012:125.707,61.093:125.768,
            61.173:125.829,61.254:126.013,61.334:126.074,61.415:126.872,61.495:126.933,61.576:127.179,61.657:127.426,61.737:127.549,61.818:127.796,61.899:127.858,
            61.979:128.416,62.06:128.54,62.141:129.098,62.222:129.223,62.302:129.347,62.383:129.472,62.464:129.534,62.545:129.784,62.626:129.847,62.707:130.16,
            62.787:130.537,62.868:130.6,62.949:130.663,63.03:130.852,63.111:130.978,63.192:132.304,63.273:132.557,63.354:132.557,63.435:132.81,63.517:133.001,
            63.598:133.192,63.679:133.319,63.76:133.574,63.841:134.339,63.922:135.106,64.003:135.682,64.085:136.386,64.166:136.707,64.247:137.156,64.328:137.928,
            64.41:138.121,64.491:138.507,64.572:139.992,64.654:140.056,64.735:140.38,64.816:140.704,64.898:141.028,64.979:141.417,65.06:141.873,65.142:142.068,
            65.223:142.329,65.305:142.981,65.386:143.047,65.468:143.308,65.549:143.832,65.631:143.898,65.712:144.029,65.794:144.095,65.875:144.095,65.957:144.556,
            66.038:144.82,66.12:144.953,66.201:145.085,66.283:145.549,66.364:145.681,66.446:146.943,66.528:147.408,66.609:147.675,66.691:148.141,66.772:148.675,
            66.854:149.41,66.936:149.544,67.017:149.879,67.099:150.482,67.181:151.556,67.262:151.893,67.344:155.258,67.426:155.932,67.507:156.741,67.589:157.146,
            67.67:157.282,67.752:157.62,67.834:157.756,67.915:158.231,67.997:158.639,68.079:158.775,68.16:159.047,68.242:159.456,68.323:159.593,68.405:160.345,
            68.487:164.931,68.568:175.484,68.65:177.68,68.731:179.397,68.813:180.085,68.894:180.085,68.976:180.291,69.057:180.706,69.139:180.775,69.22:181.051,
            69.302:181.259,69.383:182.091,69.465:182.161,69.546:182.23,69.627:182.717,69.709:182.787,69.79:183.066,69.871:183.136,69.953:183.345,70.034:183.485,
            70.115:183.626,70.196:183.766,70.277:183.836,70.358:184.117,70.439:184.258,70.52:184.399,70.601:185.034,70.682:186.165,70.763:186.942,70.844:187.084,
            70.924:187.155,71.005:187.723,71.086:187.865,71.166:188.149,71.247:188.149,71.327:188.363,71.408:188.577,71.488:188.934,71.568:189.006,71.648:189.149,
            71.728:189.579,71.808:189.651,71.888:189.795,71.968:190.514,72.047:190.874,72.127:191.235,72.206:192.173,72.286:192.245,72.365:192.39,72.444:192.39,
            72.523:192.535,72.602:193.115,72.681:193.333,72.759:194.569,72.838:194.642,72.916:194.934,72.994:195.663,73.072:196.32,73.15:196.759,73.227:196.979,
            73.304:197.198,73.382:198.005,73.459:198.519,73.535:198.887,73.612:199.328,73.688:199.77,73.764:199.991,73.84:200.286,73.916:202.207,73.991:202.355,
            74.066:202.651,74.14:202.948,74.215:203.838,74.289:203.986,74.362:204.284,74.436:204.507,74.509:204.805,74.581:205.699,74.653:205.774,74.725:205.998,
            74.796:206.073,74.867:206.222,74.937:206.447,75.007:206.822,75.076:207.872,75.144:208.023,75.212:208.474,75.279:208.624,75.346:208.7,75.411:209.076,
            75.476:209.152,75.539:209.68,75.602:210.134,75.663:210.285,75.723:210.361,75.781:212.103,75.837:212.482,75.891:212.558,75.944:212.558,75.994:213.546,
            76.043:213.774,76.089:213.85,76.134:214.154,76.176:214.611,76.216:214.687,76.254:214.764,76.29:214.916,76.324:215.221,76.356:216.061,76.385:216.214,
            76.412:216.29,76.438:216.902,76.461:217.054,76.482:217.36,76.501:217.819,76.518:218.278,76.533:218.737,76.546:221.263,76.557:221.57,76.567:221.723,
            76.575:221.876,76.581:222.259,76.586:223.178,76.589:223.714,76.591:224.25,76.593:224.556,76.593:226.012,76.593:226.548}

        self.keys = list(self.table.keys())
        self.values = list(self.table.values())

    def get_distance(self, velocity):
        res = bisect.bisect_left(self.keys, velocity)
        return self.values[res]

    pass