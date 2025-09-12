# Changelog

## [1.8.3](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.8.2...strimzi-kafka-connect-v1.8.3) (2025-09-12)


### Bug Fixes

* docker image builds exit with non-zero code if curl fails ([#370](https://github.com/miracum/util-images/issues/370)) ([dffa350](https://github.com/miracum/util-images/commit/dffa350a933cc7edfdce046c56543c7c6b48d3af))


### Chores & Updates

* **deps:** update all non-major dependencies ([#345](https://github.com/miracum/util-images/issues/345)) ([50a4db7](https://github.com/miracum/util-images/commit/50a4db7da910f4714cc4d334bfa480d712089dc6))
* **deps:** update dependency com.microsoft.sqlserver:mssql-jdbc to v13 ([#363](https://github.com/miracum/util-images/issues/363)) ([58ae572](https://github.com/miracum/util-images/commit/58ae5726a1df883bebb0e90e706c517b9c406c0a))
* **deps:** updates kafka to 3.9.1 ([#368](https://github.com/miracum/util-images/issues/368)) ([47c16fd](https://github.com/miracum/util-images/commit/47c16fde5a3999a3f0d45c696e708596ef96f5e0))
* **master:** release apache-superset 1.9.3 ([#333](https://github.com/miracum/util-images/issues/333)) ([773f940](https://github.com/miracum/util-images/commit/773f940026bdfcb5267e9f370574c3e8c8be31fd))
* **master:** release warehousekeeper 0.1.14 ([#334](https://github.com/miracum/util-images/issues/334)) ([5c291be](https://github.com/miracum/util-images/commit/5c291be253dd6224cd6eb3664a98bd79f3299409))

## [1.8.2](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.8.1...strimzi-kafka-connect-v1.8.2) (2025-07-13)


### Chores & Updates

* **deps:** use non-deprecated python oracle and updated strimzi connect ([#330](https://github.com/miracum/util-images/issues/330)) ([ec2c085](https://github.com/miracum/util-images/commit/ec2c085d610467abeb0456de2e96833880497435))

## [1.8.1](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.8.0...strimzi-kafka-connect-v1.8.1) (2025-07-12)


### Bug Fixes

* **deps:** update all non-major dependencies ([#317](https://github.com/miracum/util-images/issues/317)) ([905465d](https://github.com/miracum/util-images/commit/905465d8d05e80e01e4e5399c8013a3e633bc508))
* **deps:** update all non-major dependencies ([#326](https://github.com/miracum/util-images/issues/326)) ([ec8e320](https://github.com/miracum/util-images/commit/ec8e320227c7123e87b41b4ee9304addbd566134))


### Chores & Updates

* **deps:** update dependency com.oracle.database.jdbc:ojdbc11 to v23 ([#327](https://github.com/miracum/util-images/issues/327)) ([323cc91](https://github.com/miracum/util-images/commit/323cc91f9dd14664f70ea0a9228ecf83ddba47f8))
* **deps:** update dependency org.apache.kafka:connect-file to v4 ([#328](https://github.com/miracum/util-images/issues/328)) ([65d5139](https://github.com/miracum/util-images/commit/65d51392124b2410dc3ada218e315ec4711c7ff1))

## [1.8.0](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.7.0...strimzi-kafka-connect-v1.8.0) (2025-05-25)


### Features

* added trino, fixed dsf, renovate connect deps ([#142](https://github.com/miracum/util-images/issues/142)) ([d0bcf7d](https://github.com/miracum/util-images/commit/d0bcf7d6e303eae01c9ed8011e57941887a9c99f))


### Bug Fixes

* **deps:** update all non-major dependencies ([#219](https://github.com/miracum/util-images/issues/219)) ([c4447a4](https://github.com/miracum/util-images/commit/c4447a4209168a08b7e6d603d743199e890a89ee))
* **deps:** update all non-major dependencies ([#283](https://github.com/miracum/util-images/issues/283)) ([f60ff55](https://github.com/miracum/util-images/commit/f60ff559e16df2d6d90cc1df9489d48042fada5d))
* ENV -&gt; ARG ([5618682](https://github.com/miracum/util-images/commit/5618682e58536475a6244bd4742e084d3a9719d7))
* quote curls ([2385988](https://github.com/miracum/util-images/commit/23859889b32b6a013bd042d0aa45dc1317a47bb1))


### Chores & Updates

* **deps:** update all non-major dependencies ([#127](https://github.com/miracum/util-images/issues/127)) ([fac5031](https://github.com/miracum/util-images/commit/fac50314ab1502367e2f983eadf2aacb5a5cc822))
* **deps:** update all non-major dependencies ([#202](https://github.com/miracum/util-images/issues/202)) ([137491c](https://github.com/miracum/util-images/commit/137491c1ceb07d62c9386eddb7e2c0980f78550f))
* **deps:** update quay.io/strimzi/kafka:0.41.0-kafka-3.6.1 docker digest to 610c91e ([#105](https://github.com/miracum/util-images/issues/105)) ([bf021e3](https://github.com/miracum/util-images/commit/bf021e371154e8b790826d54e11b3ac4f9c4f05e))
* **deps:** update quay.io/strimzi/kafka:0.45.0-kafka-3.8.0 docker digest to 1fb0cac ([#242](https://github.com/miracum/util-images/issues/242)) ([379c201](https://github.com/miracum/util-images/commit/379c20161753139a4c96315cece6dea5972ab808))
* **hadolint:** fix hadolint complaints in strimzi connect ([#146](https://github.com/miracum/util-images/issues/146)) ([6a72909](https://github.com/miracum/util-images/commit/6a72909707f1e60cb665eca9507a401dc706ff43))
* **master:** release dsf-bpe-full 1.5.1 ([#185](https://github.com/miracum/util-images/issues/185)) ([c482910](https://github.com/miracum/util-images/commit/c482910bc6099ede6c223b2444d3732b5a9f5214))
* **master:** release warehousekeeper 0.1.12 ([#257](https://github.com/miracum/util-images/issues/257)) ([ab5ee7a](https://github.com/miracum/util-images/commit/ab5ee7a4c6c3877bde4922aa7736a9550b0f9574))
* **renovate:** drop confluent packages from renovation ([94195cf](https://github.com/miracum/util-images/commit/94195cfe366dcc2fd7e76c3182534bad27489a91))
* **renovate:** fix data sources ([bb1f946](https://github.com/miracum/util-images/commit/bb1f94670ee42f1c76809a99f0bbc386001ed69f))

## [1.7.0](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.6.0...strimzi-kafka-connect-v1.7.0) (2024-05-21)


### Features

* update Spark to 3.5 and Delta to 3.2 ([#62](https://github.com/miracum/util-images/issues/62)) ([2e75f0f](https://github.com/miracum/util-images/commit/2e75f0f74a24309f70e9b2f70cce8778d606b0a6))

## [1.6.0](https://github.com/miracum/util-images/compare/strimzi-kafka-connect-v1.5.2...strimzi-kafka-connect-v1.6.0) (2024-04-06)


### Features

* first commit ([67d35ed](https://github.com/miracum/util-images/commit/67d35eda3161a81101a7dae0a4709a64863b04d7))


### Bug Fixes

* switch to release-please ([#26](https://github.com/miracum/util-images/issues/26)) ([b33f8fc](https://github.com/miracum/util-images/commit/b33f8fc20e99216e7242e47102ef36830ce9cbbc))
