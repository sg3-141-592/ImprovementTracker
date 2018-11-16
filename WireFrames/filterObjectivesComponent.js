Vue.component('filter-objectives', {
    props: {objectives : Array},
    template:
    `
    <b-form-group label="Objective">
        <b-form-checkbox-group v-model="objFilterSelected">
            <b-form-checkbox v-for="objective in objectives" 
                :value="objective.name" :key="objective.id">
                {{ objective.name }}
            </b-form-checkbox>
        </b-form-checkbox-group>
    </b-form-group>
    `,
    data: function () {
        return {
            objFilterSelected: []
        }
    }
})