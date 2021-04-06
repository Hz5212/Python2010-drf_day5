<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <a href="javascript:;" @click="user_logout">安全退出</a>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>{{admin_name}},欢迎您访问百知教育管理系统!!</h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>

                    <tr class="row1" v-for = "(emp,index) in JSON.parse(emp_list)":key="index">
                        <td>{{ index+1 }}</td>
                        <td>{{ emp.emp_name }}</td>
                        <td><img src=" " style="height: 60px;"></td>
                        <td>{{ emp.salary }}</td>
                        <td>{{ emp.age }}</td>
                        <td><a href="#" @click="delete_emp(index+1)">删除员工</a>&nbsp;<a href="">更新员工</a></td>
                    </tr>

                </table>
                <p>
                    <input type="button" class="button" value="添加"/>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Index",
        data() {
            return {
                admin_name: '',
                emp_list : '',
                id :  '',
            }
        },
        methods: {
            // 完成用户注销
            user_logout() {
                //删除用户信息
                sessionStorage.removeItem('name')
                sessionStorage.removeItem('id')
                //跳转到登录耶
                this.$router.push("/login")
            },
            // 获取员工列表数据
            get_emp_list() {
                // 向后端发送请求，获取数据
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/employees/",
                    method: "get",
                }).then(res=>{
                  if (res.data) {
                      console.log(res.data);
                      this.$message.success("获取到的信息如下")
                        sessionStorage.emp = JSON.stringify(res.data)
                        this.emp_list = sessionStorage.emp;
                        console.log(this.emp_list);
                  } else {
                         this.$message.error("信息有误（in for）")
                    }
                }).catch(error=>{
                    this.$message.error("信息有误(error)")
                })
            },

            // 删除员工列表数据
            delete_emp(pk){
              console.log(pk)
                // 向后端发送请求，删除数据
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/employees/",
                    method: "post",
                    params: {
                        id : pk,
                    }
                }).then(res=>{
                  if (res.data) {
                      console.log(res.data);
                      this.$message.success("删除成功")
                      // 删除成功则跳转到首页
                      this.$router.push("/index")
                      // 刷新页面数据
                      location. reload()
                  } else {
                         this.$message.error("删除失败")
                    }
                }).catch(error=>{
                    this.$message.error("删除失败")
                })
            },


        },


        // 在加载组件前判断用户是否登录，登录可以访问，未登录不能访问
        created() {
            let id = sessionStorage.id;
            if (id) {
                this.admin_name = sessionStorage.name;
            } else {
                this.$message.error("对不起，您还未登录，请登录后在访问");
                this.$router.push("/login");
            }

            // 调用获取员工列表数据的方法
            this.get_emp_list()

        },
    }
</script>

<style scoped>

</style>
