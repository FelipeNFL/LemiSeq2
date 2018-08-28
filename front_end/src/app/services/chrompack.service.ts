import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable()
export class ChromPackService {

    constructor(private http: HttpClient) { }

    public upload(title, fileList): any{
        let file: File = fileList[0];
        let formData: FormData = new FormData();

        formData.append('file', file, file.name);
        formData.append('title', title)

        let headers = new HttpHeaders();

        headers.append('Content-Type', 'multipart/form-data');
        headers.append('Accept', 'application/json');

        return this.http.post(`${environment.bioprocess_api}/chrompack`, formData, {headers: headers})
    }

    public getList(): any{
        return this.http.get(`${environment.bioprocess_api}/chrompack/all`);
    }

    public delete(id: String): any {
        return this.http.delete(`${environment.bioprocess_api}/chrompack/${id}`);
    }

}