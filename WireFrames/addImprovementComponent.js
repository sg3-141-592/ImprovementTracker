Vue.component('add-improvement', {
    template:
    `
    <!-- Main form-->
    <div>
        <b-btn v-b-modal.addImpWindow>Add Improvement</b-btn>
        <b-modal id="addImpWindow"
                 title="New Improvement"
                 size="lg"
                 >
            <!-- -->
            <form>

                <!-- Title/Description -->
                <div class="form-group row">
                    <label class="col-sm-2 col-form-label">Title</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" placeholder="...">
                    </div>
                </div>

                <div class="form-group row">
                    <label class="col-sm-2 col-form-label">Description</label>
                    <div class="col-sm-10">
                        <textarea rows="3" class="form-control" placeholder="..."></textarea>
                    </div>
                </div>

                <!-- Predicted Benefits -->
                <div class="form-group row">
                    <label class="col-sm-2 col-form-label">Benefits</label>
                    <div class="col-sm-10">
                        
                        <!-- Add new benefit dropdown -->
                        <add-benefits :benefits=benefitsData></add-benefits>

                    </div>
                </div>

            </form>
        </b-modal>
    </div>
    `,
    data: function () {
        return {
            benefitsData: null
        }
    },
    mounted () {
        // Load benefits data
        axios
            .get("http://127.0.0.1:8080/improvements/benefits")
            .then(response => (this.benefitsData = response.data))
            .catch(error => console.log(error));
    }
});