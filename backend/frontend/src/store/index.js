import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    is_login: false,

    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    select_file: '',
    select_sheet: '',

    xlsx_name: {},
  },

  mutations: {
    setLogin(state, payload){
      state.is_login = payload;
    },

    set_Select_Date(state, payload){
      state.date = payload
    },
    set_Select_File(state, payload){
      state.select_file = payload
    },
    set_Select_Sheet(state, payload){
      state.select_sheet = payload
    },
    set_Xlsx_Name(state, payload){
      state.xlsx_name = payload
    },
  },
  actions: {
  },
  modules: {
  }
})
