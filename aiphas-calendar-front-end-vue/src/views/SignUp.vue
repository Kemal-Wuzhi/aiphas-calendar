<template>
  <div class="container py-5">
    <form class="w-100" @submit.prevent.stop="handleSubmit">
      <div class="text-center mb-4">
        <h1 class="h3 mb-3 font-weight-normal">
          Sign Up
        </h1>
      </div>

      <div class="form-label-group mb-2">
        <label for="email">Email</label>
        <input
          id="email"
          v-model="email"
          name="email"
          type="email"
          class="form-control"
          placeholder="Email"
          required
          autofocus
        >
      </div>

      <div class="form-label-group mb-3">
        <label for="name">Name</label>
        <input
          id="name"
          v-model="name"
          name="name"
          type="name"
          class="form-control"
          placeholder="Name"
          required
        >
      </div>

      <div class="form-label-group mb-3">
        <label for="password">Password</label>
        <input
          id="password"
          v-model="password"
          name="password"
          type="password"
          class="form-control"
          placeholder="Password"
          required
        >
      </div>

      <button
        class="btn btn-lg btn-primary btn-block mb-3"
        type="submit"
      >
        Submit
      </button>

      <div class="text-center mb-3">
        <p>
          <router-link to="/signin">Sign In</router-link>
        </p>
      </div>

      <p class="mt-5 mb-3 text-muted text-center">
 
      </p>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      name: '',
      password: ''
      
    }
  },
  methods:{
    handleSubmit(){
        const data = JSON.stringify({
            email:this.email,
            name:this.name,
            password:this.password
        })
    console.log(data)
    }
  }
}
</script>