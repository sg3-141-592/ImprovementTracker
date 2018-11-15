// Add benefits component
Vue.component('add-benefits', {
    props: {benefits : Array},
    template:
    `
    <div class="container">
        <!-- Add new benefit dropdown -->
        <div class="form-group row">
            <b-form-select class="col-sm-10" v-model="selectedItem">
                <option v-for="benefit in benefits" :key=benefit.id :value=benefit.id>
                    {{ benefit.name }}
                </option>
            </b-form-select>
            <div class="col-sm-2">
                <b-button @click="addBenefit">Add</b-button>
            </div>
        </div>
        <!-- Modify benefits -->
        <div v-for="newBenefit in addedBenefits">
            <div class="form-group row">
                <b-card no-body class="w-100" border-variant="secondary">
                    <b-card-header>
                        {{ getBenefit(newBenefit.benefitType) }}
                    </b-card-header>
                    <b-card-body>
                        <textarea rows="3" class="form-control">{{ newBenefit.description }}</textarea>
                    </b-card-body>
                </b-card>
            </div>
        </div>
    </div>
    `,
    data: function () {
        return {
            addedBenefits: [{
                benefitType: 1,
                description: "Users have access to the best tool for doing merges"
            }],
            selectedItem: null
        }
    },
    methods: {
        getBenefit: function (id)
        {
            // Find the matching item
            var match = "Error";
            if(this.benefits != null){
                this.benefits.forEach(function(element) {
                    if(element.id == id){
                        match = element.name;
                    }
                });
            }
            else
            {
                console.log("this.benefits = null");
            }
            return match;
        },
        addBenefit: function ()
        {
            this.addedBenefits.push({ benefitType: this.selectedItem, description: "..." });
        }
    }
});