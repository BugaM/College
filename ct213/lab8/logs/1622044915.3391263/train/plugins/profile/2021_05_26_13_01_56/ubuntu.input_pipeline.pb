	F\ ??Q@F\ ??Q@!F\ ??Q@	??uMշ????uMշ??!??uMշ??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$F\ ??Q@?H???B@A&??[XQ@Ybg
?װ?*	bX949?@2~
GIterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap[0]::Generatort(CULe@!ǳ???X@)t(CULe@1ǳ???X@:Preprocessing2g
0Iterator::Model::MaxIntraOpParallelism::Prefetchˆ5?Ea??!??2????)ˆ5?Ea??1??2????:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism4e??E??!d?(???)<?2T?T??1"=?#J??:Preprocessing2F
Iterator::Model?¼Ǚ&??!ʿ M.??)??U?Zn?1-??ncH??:Preprocessing2p
9Iterator::Model::MaxIntraOpParallelism::Prefetch::FlatMapB	3m?j@!?ˊG?X@).8??_?f?1?$??9??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is POTENTIALLY input-bound because 3.7% of the total step time sampled is spent on 'All Others' time (which could be due to I/O or Python execution or both).no*no9??uMշ??I???
?X@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?H???B@?H???B@!?H???B@      ??!       "      ??!       *      ??!       2	&??[XQ@&??[XQ@!&??[XQ@:      ??!       B      ??!       J	bg
?װ?bg
?װ?!bg
?װ?R      ??!       Z	bg
?װ?bg
?װ?!bg
?װ?b      ??!       JCPU_ONLYY??uMշ??b q???
?X@