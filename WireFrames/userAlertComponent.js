// User alert component
Vue.component('user-alert', {
    props: ['alert-msg'],
    template:
    `
    <b-alert show dismissible @dismissed="dismissAlert">
        {{ alertMsg }}
    </b-alert>
    `,
    methods: {
        // Mark an alert as read so user doesn't see it more than once
        dismissAlert: function ()
        {
            console.log(this.key);
            axios
                .post("http://127.0.0.1:8080/improvements/alerts", {
                    alertNum: this.$vnode.key
                })
                .then(response => console.log(response))
                .catch(error => console.log(error));
        }
    }
});