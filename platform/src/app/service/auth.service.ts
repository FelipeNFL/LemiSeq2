import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/do';

import { environment } from './../../environments/environment';

@Injectable()
export class AuthService {

  constructor(private http: HttpClient) { }

  check(): boolean {
    return true;
  }

  login(credentials: {username: string, password: string}) : Observable<boolean> {
    return this.http.post<any>(`$(environment.auth_url)/token`, credentials)
      .do(data => {
        localStorage.setItem('token', data.token);
      });
  }

}
