<template>
  <div>
    <h2>pcap-analysis-tool</h2>
    <div class="text-area">
      <el-upload
        class="upload-button"
        ref="upload"
        action="http://127.0.0.1:5000/pcap/upload"
        :on-success="handleFiles"
        auto-upload
        :limit="1"
        accept=".pcap"
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
      <el-divider content-position="right">By minyue</el-divider>
      <el-dialog
        title="顺序图"
        width="70%"
        center
        :visible.sync="dialogTableVisible"
        :before-close="beforeCloseDialog"
      >
          <div class="dialog" id="pdfDom">
            <sequence-diagram :data-list="dataList" @line-click="showItemMsg"/>
          </div>
          <el-dialog
            width="30%"
            title="亲，关闭页面需要重新上传解析哦！ 您可选择下载PDF～"
            :visible.sync="innerVisible"
            append-to-body>
            <el-button type="primary" @click="getPdf('文件名')">导出(pdf)</el-button>
            <el-button type="warning" @click="innerVisible = false; dialogTableVisible = false">关闭</el-button>
          </el-dialog>
      </el-dialog>
      <div class="msg-table">
        <el-table :data="dataList">
          <el-table-column prop="from" label="源地址" width="200" />
          <el-table-column prop="to" label="目的地址" width="200" />
          <el-table-column prop="note" label="内容" width="600" />
          <el-table-column prop="label" label="时间" />
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import { Message } from 'element-ui'
import SequenceDiagram from '@/components/SequenceDiagram.vue'
export default {
  name: 'pcapanalysis',
  data () {
    return {
      isUpload: false,
      dataList: [{
        label: Date.now(),
        from: 'null',
        to: 'null',
        note: '',
        isDash: 0
      }],
      dialogTableVisible: false,
      innerVisible: false
    }
  },
  components: {
    SequenceDiagram
  },
  methods: {
    onSubmit () {
      this.axios
        .get('http://127.0.0.1:5000/pcap/analysis')
        .then(res => {
          console.log('res', res.data)
          // debugger
          this.initData(res.data)

          this.dialogTableVisible = true
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
      this.$refs['upload'].clearFiles()
    },
    initData (data) {
      const arr = Object.values(data).reduce(
        (pre, cur) => [...pre, doaa(JSON.parse(cur))],
        []
      )
      function doaa (bobj) {
        const {time, src, sport, dst, dport, content} = bobj

        return {
          label: time,
          from: `${src}:${sport}`,
          to: `${dst}:${dport}`,
          note: content,
          isDash: 0
        }
      }
      arr[arr.length - 1].isDash = 1
      arr[arr.length - 2].isDash = 1
      this.dataList = arr
      console.log(arr)
    },
    showItemMsg (index, data) {
      console.log('data', data)
      alert('当前节点信息' + data.note)
    },
    beforeCloseDialog (done) {
      this.innerVisible = true
    }
  }
}
</script>

<style lang="less" scoped>
@color: midnightblue;
.text-area {
  margin-left: 20%;
  margin-right: 20%;
}
div {
  color: @color;
}
.msg-table {
  width: 800px;
  height: 300px;
  margin: 20px;
}
.dialog {
  width: 100%;
  height: 90vh;
}
</style>
