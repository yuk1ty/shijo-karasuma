<template lang="pug">
  // register
  div.stock_register
    h2.stock_register__title Register Stock

    div.stock_register__form
      div.stock_register__form__code
        label Stock Code:
        input(placeholder='Stock Code', v-model='stock.code')

      div.stock_regsiter__form__name
        label Stock Name:
        input(placeholder='Stock Name', v-model='stock.name')

      div.stock_resgister__form__type
        label Type:
        select(v-model='stock.type')
          option(value='IX') Index
          option(value='ID') Individual

      button(type='button', name='button', v-on:click='addIssue()') Register
</template>

<script>
import { Stock } from '@/context/entity/stock'
import moment from 'moment'

export default {
  name: 'stock-register',
  data () {
    return {
      stock: {
        code: '',
        name: '',
        type: ''
      }
    }
  },
  methods: {
    addIssue: function () {
      const self = this
      let moment = require("moment")
      const toSave = new Stock(self.stock, moment().format("YYYY-MM-DD HH:mm:ss"), '0')
      self.axios.post('/api/stock/save', toSave.toJson()).then((res) => {
        // TODO ちゃんとしたダイアログが立ち上がるようにするべき
        alert("登録が完了しました。")
        console.log(res)
      }).catch((res) => {
        console.log("error!: " + res)
      })
    }
  }
}
</script>

<style>
</style>
