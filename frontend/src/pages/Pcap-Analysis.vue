<template>
    <div>
        <h2>pcap-analysis-tool</h2>
        <div id="text-area">
            <el-input type="textarea" :rows="10" placeholder="请输入内容" v-model="textarea">
            </el-input>
            <div id="img">
                <el-input v-model="pic" placeholder="输出内容" disabled></el-input>
            </div>
            <div id="operation">
                <el-row>
                    <el-button type="primary" @click="onSubmit" round>生成</el-button>
                    <el-button type="success" @click="onDownload" round>下载</el-button>
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
      pic: [],
      pageTitle: 'Flask Vue Word Cloud'
    }
  },
  methods: {
    onSubmit () {
      var param = {
        'word': this.textarea
      }
      this.axios.post('/pcap/analysis', param).then(
        res => {
          this.pic = res.data
          console.log(res.data)
        }
      ).catch(res => {
        console.log(res.data.res)
      })
    },
    onDownload () {
      const imgUrl = 'data:image/png;base64,' + this.pic
      const a = document.createElement('a')
      a.href = imgUrl
      a.setAttribute('download', 'word-cloud')
      a.click()
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
