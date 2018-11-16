Vue.component('add-improvement', {
    template:
    `
    <!-- Main form-->
    <div class="card">
        <div class="card-header">
            New Improvement
        </div>
        <div class="card-body">
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

                <!-- Submit/Close Buttons -->
                <div class="form-group row">
                    <div class="col">

                    </div>
                    <div class="col">
                        <div class="float-right">
                            <b-button>Submit</b-button>
                            <b-button>Close</b-button>
                        </div>
                    </div>
                </div>

            </form>
        </div>
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