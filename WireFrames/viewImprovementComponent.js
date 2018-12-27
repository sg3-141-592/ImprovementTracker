Vue.component('view-improvement', {
    props: ['improvementId'],
    template:
    `
    <b-modal    title="Improvement View"
                size="lg"
                >
        <!-- -->
        <form>

            <!-- Title/Description -->
            <div class="form-group row">
                <label class="col-sm-2 col-form-label">Title</label>
                <div class="col-sm-10">
                    <b-form-input type="text" v-model="improvementData.name" placeholder="..."></b-form-input>
                </div>
            </div>

            <div class="form-group row">
                <label class="col-sm-2 col-form-label">Description</label>
                <div class="col-sm-10">
                    <b-form-textarea v-model="improvementData.description" placeholder="..." :rows="3"></b-form-textarea>
                </div>
            </div>

            <!-- Predicted Benefits -->
            <div class="form-group row">
                <label class="col-sm-2 col-form-label">Benefits</label>
                <div class="col-sm-10">
                    
                    <!-- Add new benefit dropdown -->
                    <add-benefits :benefits=improvementData.benefitsData></add-benefits>

                </div>
            </div>

        </form>
    </b-modal>
    `,
    data: function () {
        return {
            improvementData: null
        }
    },
    mounted () {
        
    },
    methods: {

    }
})