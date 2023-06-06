import { Component } from '@angular/core';
import { ApiService } from '../Services/API/api.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  file: File | undefined;

  constructor(private api: ApiService) { }

  onSubmit() {
    console.log('submit')
  }

  onFileChange(event: any) {
    const fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      this.file = fileList[0];

    }

  }

  uploadFile() {
    if (this.file && this.file.type.startsWith('image/')) {
      // File is an image, perform upload logic
      console.log(this.file)
     const dataObj = new FormData();
     dataObj.append('file', this.file)
      this.api.post('/file_operation/upload_file/', dataObj).subscribe(res=>{
        console.log(res)
      })

    } else {
      console.log('Please select a valid image file.');
    }
  }


}
