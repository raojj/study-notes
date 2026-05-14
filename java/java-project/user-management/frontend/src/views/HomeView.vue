<template>
  <div>
    <el-button @click="add" type="primary">
      Add
    </el-button>
  </div>

  <el-dialog
      v-model="dialogVisible"
      title="Tips"
      width="500"
      :before-close="handleClose"
  >
    <span>
        <el-form
            :label-position="labelPosition"
            label-width="auto"
            :model="formLabelAlign"
            style="max-width: 600px"
        >
      <el-form-item label="Name" :label-position="itemLabelPosition">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="region" :label-position="itemLabelPosition">
        <el-input v-model="form.region" />
      </el-form-item>
      <el-form-item label="job" :label-position="itemLabelPosition">
        <el-input v-model="form.job" />
      </el-form-item>
    </el-form>
    </span>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="save">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>

  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column prop="name" label="Name" />
    <el-table-column prop="region" label="Region" />
    <el-table-column prop="job" label="Job" />
    <el-table-column fixed="right" label="Operations" min-width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleEdit(scope.row)">Edit</el-button>
        <el-popconfirm title="确定删除吗?" @confirm="handleDelete(scope.row)">
          <template #reference>
            <el-button link type="primary" size="small">Delete</el-button>
          </template>
        </el-popconfirm>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>

import request from '@/utils/request'

export default {
  name: 'HomeView',
  data(){
    return {
      form: {},
      dialogVisible: false,
      tableData: []
    }
  },
  created() {
    this.load()
  },
  methods: {
    load(){
      request.get("http://localhost:9090/user").then(
          res=>{
            this.tableData=res
          }
      )
    },
    add(){
      this.dialogVisible = true
    },
    save(){
      request.post("http://localhost:9090/user", this.form).then(
          ()=>{
            this.dialogVisible = false
            this.load()
          }
      )
    },
    handleEdit(row){
      this.form = JSON.parse(JSON.stringify(row))
      this.dialogVisible = true
    },
    handleDelete(row){
      request.delete(`http://localhost:9090/user/${row.id}`).then(
          ()=>{
            this.load()
          }
      )
    }
  }
}
</script>
