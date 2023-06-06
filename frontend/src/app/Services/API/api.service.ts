import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class ApiService {

    url = 'http://localhost:4201';

    constructor(private http: HttpClient) {
    }

    post(endpoint: string, body: any, reqOpts?: any) {
        return this.http.post(this.url + endpoint, body, reqOpts);
    }

    get(endpoint: string, params?: any, reqOpts?: any) {
        if (!reqOpts) {
            reqOpts = {
                params: new HttpParams()
            };
        }

        // Support easy query params for GET requests
        if (params) {
            reqOpts.params = new HttpParams();
            for (const k in params) {
                reqOpts.params = reqOpts.params.set(k, params[k]);
            }
        }
        return this.http.get(this.url + '?' + endpoint, reqOpts);

    }
}
