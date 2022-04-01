<template>
  <div>
    <h2>pcap-analysis-tool</h2>
    <div id="text-area">
      <el-input
        type="textarea"
        :rows="10"
        placeholder="请输入内容"
        v-model="textarea"
      >
      </el-input>
      <div id="img">
        <el-table :data="dataTable" style="width: 500px">
          <el-table-column prop="type" label="类型" width="180" />
          <el-table-column prop="content" label="内容" width="180" />
          <el-table-column prop="time" label="时间" />
        </el-table>
      </div>
      <div id="operation">
        <el-row>
          <el-button type="success" @click="onUpload" round>上传</el-button>
          <el-button type="primary" @click="onSubmit" round>生成</el-button>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'pcapanalysis',
  data () {
    return {
      textarea: '',
      dataTable: [{
        type: '暂无数据',
        content: '暂无数据',
        time: Date.now()
      }]
    }
  },
  methods: {
    onSubmit () {
      var param = {
        word: this.textarea
      }
      this.axios
        .post('http://127.0.0.1:5000/pcap/analysis', param)
        .then(res => {
          const arr = Object.values(res.data).reduce((pre, cur) => [...pre, JSON.parse(cur)], [])
          this.dataTable = arr
          console.log(arr)
        })
        .catch(res => {
          console.log(res.data)
        })
    },
    onDownload () {
    }
  }
}
</script>

<style scoped>
#text-area {
  margin-left: 20%;
  margin-right: 20%;
}
#operation {
  margin-top: 20px;
}
#img {
  width: 800px;
  height: 300px;
  margin: 20px;
}
</style>
