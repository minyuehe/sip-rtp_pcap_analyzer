<template>
  <div>
    <h2>pcap-analysis-tool</h2>
    <div class="text-area">
      <el-upload
        class="upload-button"
        ref="upload"
        action="http://127.0.0.1:5000/pcap/upload"
        :on-success="handleFiles"
        :before-upload="beforeUpload"
        accept=".pcap"
        :limit="1"
        :show-file-list="false"
      >
        <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
        <div slot="tip" class="el-upload__tip">
          只能上传pcap文件
        </div>
      </el-upload>
      <div class="operation">
        <el-button
          type="primary"
          @click="onSubmit"
          round
          :disabled="isUpload"
        >
          生成
        </el-button>
      </div>
      <div class="msg-table">
        <el-table :data="dataTable">
          <el-table-column prop="type" label="类型" width="50" />
          <el-table-column prop="content" label="内容" width="600" />
          <el-table-column prop="time" label="时间" />
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import { Message } from 'element-ui'
export default {
  name: 'pcapanalysis',
  data () {
    return {
      dataTable: [
        {
          type: '暂无数据',
          content: '暂无数据',
          time: Date.now()
        }
      ],
      isUpload: false
    }
  },
  methods: {
    onSubmit () {
      this.axios
        .get('http://127.0.0.1:5000/pcap/analysis')
        .then(res => {
          console.log('res', res)
          const arr = Object.values(res.data).reduce(
            (pre, cur) => [...pre, JSON.parse(cur)],
            []
          )

          this.dataTable = arr
          console.log(arr)
        })
        .catch(res => {
          const { data: msg } = res.response

          Message({
            message: msg,
            type: 'error',
            duration: 5 * 1000
          })
        })
      this.isUpload = true
    },
    handleFiles (resp) {
      Message({
        message: resp.msg,
        type: 'success',
        duration: 5 * 1000
      })
      this.isUpload = false
    },
    beforeUpload (file) {
      console.log('beforeUpload', file)
    }
  }
}
</script>

<style scoped>
.text-area {
  margin-left: 20%;
  margin-right: 20%;
}
/* .upload-button {
  padding: 20px;
}
.operation {
  height: 100px;
} */
.msg-table {
  width: 800px;
  height: 300px;
  margin: 20px;
}
</style>
