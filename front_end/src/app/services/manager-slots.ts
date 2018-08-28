export class ManagerSlots {

    matrix: any;

    constructor(matrix) {
        this.matrix = matrix;
    }

    getColumns() {

        const lines = this.getLinesKeys();

        if(lines.length > 0) {
        
            const firstLineKey = lines[0];
            const firstLineValue = this.matrix[firstLineKey];
        
            return Object.keys(firstLineValue);
        }

        return [];
    }

    getLinesKeys() {
        
        if (!this.matrix) {
            return [];
        }

        return Object.keys(this.matrix);
    }

}