	?8b->?S@?8b->?S@!?8b->?S@	????G???????G???!????G???"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?8b->?S@%w?Dfn@A?4}vGS@Y?pX?Q??*	???wL?@2~
GIterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap[0]::Generator???o@!B??͡X@)???o@1B??͡X@:Preprocessing2g
0Iterator::Model::MaxIntraOpParallelism::Prefetch?,?i????!7^?????)?,?i????17^?????:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism??;??J??!???(???)c?????1)RԤK??:Preprocessing2F
Iterator::Model%?c\qq??!W?_e?a??)Ӣ>?6q?1?=?????:Preprocessing2p
9Iterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap~7ݲ?@!S?jZx?X@)?,^,a?1?B??-???:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is POTENTIALLY input-bound because 3.5% of the total step time sampled is spent on 'All Others' time (which could be due to I/O or Python execution or both).no*no9????G???I?.??X@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	%w?Dfn@%w?Dfn@!%w?Dfn@      ??!       "      ??!       *      ??!       2	?4}vGS@?4}vGS@!?4}vGS@:      ??!       B      ??!       J	?pX?Q???pX?Q??!?pX?Q??R      ??!       Z	?pX?Q???pX?Q??!?pX?Q??b      ??!       JCPU_ONLYY????G???b q?.??X@