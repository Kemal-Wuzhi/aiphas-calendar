<template>
  <div id="app">
    <Navbar />
    <router-view/>
  </div>
</template>

import bootstrap
<script>
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components:{
    Navbar
  }
}
</script>

<style>

</style>
