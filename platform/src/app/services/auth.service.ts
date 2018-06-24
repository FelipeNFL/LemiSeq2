import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";

@Injectable()
export class AuthService {

    constructor(private http: HttpClient) { }

    public requestToken(email: string, password: string): any {
        return this.http.post(`${environment.auth_api}/token`, {username: email, password})
    }

    public setSession(token: string, username: string) {
        localStorage.setItem('token', token);
        localStorage.setItem('username', username);
    }

    public logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
    }

    public isLogged() {
        return Boolean(localStorage.getItem('token'));
    }
}
