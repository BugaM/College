?	??>?|^@??>?|^@!??>?|^@	??7a)N????7a)N??!??7a)N??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$??>?|^@u??<f?@A????V@Y?t"?T3??*	+?V0?@2~
GIterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap[0]::Generator?a??ma@!??4?]?X@)?a??ma@1??4?]?X@:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelismOZ???f??!?^?Ҁ???)?YI+????1?(?n???:Preprocessing2g
0Iterator::Model::MaxIntraOpParallelism::Prefetch?Z'.?+??!G?56-???)?Z'.?+??1G?56-???:Preprocessing2F
Iterator::Model^?V$&???!???i'Z??)???y7d?1?޹piJ??:Preprocessing2p
9Iterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap\Va3?e@!?Yb??X@)~oӟ?Ha?11??????:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is POTENTIALLY input-bound because 25.7% of the total step time sampled is spent on 'All Others' time (which could be due to I/O or Python execution or both).no*no9??7a)N??I??:6?X@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	u??<f?@u??<f?@!u??<f?@      ??!       "      ??!       *      ??!       2	????V@????V@!????V@:      ??!       B      ??!       J	?t"?T3???t"?T3??!?t"?T3??R      ??!       Z	?t"?T3???t"?T3??!?t"?T3??b      ??!       JCPU_ONLYY??7a)N??b q??:6?X@Y      Y@qB??A???"?
both?Your program is POTENTIALLY input-bound because 25.7% of the total step time sampled is spent on 'All Others' time (which could be due to I/O or Python execution or both).b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQ2"CPU: B 