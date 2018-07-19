import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable()
export class UserService {

    constructor(private http: HttpClient) { }

    getMetrics(): any {
        return this.http.get(`${environment.bioprocess_api}/metrics`);
    }
}