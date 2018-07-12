import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";

@Injectable()
export class AuthService {

    constructor(private http: HttpClient) { }

    public requestToken(email: string, password: string): any {
        return this.http.post(`${environment.auth_api}/token`, {username: email, password})
    }

    public setSession(token: string, fullname: string) {
        localStorage.setItem('token', token);
        localStorage.setItem('fullname', fullname);
    }

    public getFullname() {
        return localStorage.getItem('fullname');
    }

    public logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('fullname');
    }

    public isLogged() {
        return Boolean(localStorage.getItem('token'));
    }
}
