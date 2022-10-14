<template>
  <v-app-bar
    color="red"
    prominent
  >
    <v-app-bar-nav-icon variant="text" @click.stop="rail = !rail"></v-app-bar-nav-icon>

    <v-toolbar-title>Pokedex, GO!</v-toolbar-title>
  </v-app-bar>

  <v-navigation-drawer
    v-model="drawer"
    color="red"
    :rail="rail"
    permanent
    @click="rail = false"
  >
    <v-list

    >
      <v-list-item
        prepend-icon="mdi-magnify"
      >
        <v-text-field
          v-model="namequery"
          label="Search by Name" />
      </v-list-item>
      <v-list-item
        prepend-icon="mdi-fire"
      >
        <v-text-field
          v-model="typequery"
          label="Search by type " />
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-main>


    <v-list
    >
      <ListCard v-for="pokemon in pokemons" :pokemon="pokemon" />
    </v-list>
  </v-main>
</template>

<script>
import ListCard from './ListCard.vue'

const baseURL = ''
try {
  const baseURL = process.env.BASE_URL
}
catch(err) {
  console.log("Using default baseURL")
}

export default {
  name: 'Layout',

  components: {
    ListCard
  },

  methods: {
    async get_pokemon(namequery=null, typequery=null) {
      let nameq = namequery ? `&name=${namequery}` : ''
      let typeq = typequery ? `&type=${typequery}` : ''
      let l = await fetch(baseURL + `v1/pokemon?${nameq}${typeq}`)
      let l_json = await l.json()
      this.pokemons = l_json
    },
  },

  data: () => ({
    namequery: null,
    typequery: null,
    drawer: true,
    rail: true,
    pokemons: [],
    group: null,
  }),
  
  watch: {
    group () {
      this.drawer = false
    },

    async namequery () {
      await this.get_pokemon(this.namequery, this.typequery)
    },

    async typequery () {
      await this.get_pokemon(this.namequery, this.typequery)
    },
  },
}
</script>
