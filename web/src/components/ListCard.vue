<template>
  <v-card
    class="mx-auto"
    max-width="368"
    :color="typeColors[pokemon.type[0]]"
  >
    <v-card-item>
      <v-card-title class="text-h5">{{pokemon.num}}</v-card-title>

      <v-card-subtitle>
        <v-icon
          icon="mdi-alert"
          size="18"
          color="error"
          class="mr-1 pb-1"
        ></v-icon>

        {{pokemon.type.toString()}}
      </v-card-subtitle>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" hide-gutters no-gutters>
        <v-col
          class="text-h5"
          cols="6"
        >
          {{pokemon.name}}
        </v-col>

        <v-col cols="6" class="text-right">
          <img :src="pokemon.img" />
        </v-col>
      </v-row>
    </v-card-text>

    <!-- <v-list-item density="compact">
      <v-list-item-avatar left>
        <v-icon icon="mdi-weather-windy"></v-icon>
      </v-list-item-avatar>

      <v-list-item-subtitle>123 km/h</v-list-item-subtitle>
    </v-list-item>

    <v-list-item density="compact">
      <v-list-item-avatar left>
        <v-icon icon="mdi-weather-pouring"></v-icon>
      </v-list-item-avatar>

      <v-list-item-subtitle>48%</v-list-item-subtitle>
    </v-list-item> -->

    <v-expand-transition>
      <div v-show="expand">

        <v-list>
          <v-list-item
            v-for="key in Object.keys(pokemon)"
            :key="key"
            :title="key"
            :subtitle="JSON.stringify(pokemon[key])"
          >
          </v-list-item>
        </v-list>
      </div>
    </v-expand-transition>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn @click="expand = !expand">
        More Information
      </v-btn>
    </v-card-actions>
  </v-card>
  <br />
</template>

<script>

export default {
  name: 'ListCard',

  props: {
    pokemon: Object
  },

  data: () => ({
    //
    expand: false,
    typeColors: {
      'Electric': 'yellow-lighten-4',
      'Fire': "red-lighten-4",
      'Poison': "purple-lighten-4",
      'Water': "blue-lighten-4",
      'Fighting': "orange-lighten-4",
      'Grass': "green-lighten-4",
      'Ghost': "indigo-lighten-4",
      'Ice': "cyan-lighten-4",
      'Bug': "light-green-lighten-4",
      'Ground': "deep-orange-lighten-4",
      'Psychic': "deep-purple-lighten-4",
      'Rock': 'brown-lighten-4',
      'Dragon': 'grey-lighten-2'
    }
  }),


}

</script>