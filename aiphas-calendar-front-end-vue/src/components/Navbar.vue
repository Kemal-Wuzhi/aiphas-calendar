<template>
  <nav class="navbar navbar-expand-lg  navbar-dark bg-dark">
    <router-link
      class="navbar-brand"
      to="/"
    >
      Aiphas Calendar
    </router-link>

    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </button>

    <div
      id="navbarSupportedContent" 
      class="navbar-collapse collapse"
    >
      <div class="ml-auto d-flex align-items-center">
        <!-- is user is admin -->
        <router-link
             to="#" 
             class="text-white mr-3"
        >
         Admin Dashboard
       </router-link>

        <!-- is user is login -->
        <!-- User顯示登入者的名字 -->
          <router-link
             to="#" 
             class="text-white mr-3"
          > 
           Hello User
         </router-link>
         <button
           type="button" 
           class="btn btn-sm btn-outline-success my-2 my-sm-0"
          >
           Log Out
          </button>
      </div>
    </div>
  </nav>
</template>