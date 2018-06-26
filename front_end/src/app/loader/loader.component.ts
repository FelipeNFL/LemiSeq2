import { Component, OnInit } from '@angular/core'

@Component({
    selector: 'loader',
    templateUrl: './loader.component.html',
    styleUrls: [
        './loader.component.css'
    ]
})
export class LoaderComponent implements OnInit {
    suspensionPoints = '...';

    ngOnInit() {
        setInterval(() => this.run(), 500)
    }

    run() {
        if(this.suspensionPoints.length === 3) {
            this.suspensionPoints = '.';
        }
        else {
            this.suspensionPoints += '.';
        }
    }
}