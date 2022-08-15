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
           Hello {{User}}
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

<script>
// export default {
//   name: 'Main',
//   // components: {
//   //   TaskDetail: () => import('@/components/TaskDetail'),
//   // },
//   data: () => ({

//   }),
//   mounted() {
//     const data = this.$moment().clone();
//     this.events = [
//       { id: 1, name: 'Event 1', type: this.random(), date: data },
//       { id: 2, name: 'Event 2', type: this.random(), date: data },
//       { id: 3, name: 'Event 3', type: this.random(), date: data },
//       { id: 4, name: 'Event 4', type: this.random(), date: data.clone().add(3, 'day') },
//       { id: 5, name: 'Event 5', type: this.random(), date: data.clone().add(3, 'day') },
//       { id: 6, name: 'Event 6', type: this.random(), date: data.clone().add(6, 'day') },
//       { id: 8, name: 'Event 7', type: this.random(), date: data.clone().add(16, 'day') },
//       { id: 9, name: 'Event 7', type: this.random(), date: data.clone().add(19, 'day') },
//       { id: 10, name: 'Event 7', type: this.random(), date: data.clone().add(35, 'day') },
//     ];
//   },
//   methods: {
//     random() {
//       return this.type[Math.floor(Math.random() * this.type.length)];
//     },
//     add() {
//       const data = this.$moment().clone();
//       const maxId = Math.max(...this.events.map(item => item.id)) + 1;
//       this.events.push({ id: maxId, name: 'Event ' + maxId, type: this.random(), date: data.clone().add(maxId - 10, 'day') });
//     },
//   },
// };

</script>